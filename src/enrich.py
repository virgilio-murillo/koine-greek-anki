"""Enrich lessons: LLM reviews full lesson script and rewrites naturally.
Code provides verified data — LLM writes the lesson content."""
import json, csv, boto3, copy, sys, os, random
sys.path.insert(0, ".")

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
MODEL = 'us.anthropic.claude-sonnet-4-20250514-v1:0'

# --- Load reference data ---
with open('data/matthew/compounds_enriched.json') as f:
    compounds = json.load(f)

comp_map = {}
for c in compounds:
    comp_map[c['lemma']] = c
    for p in c['components']:
        comp_map.setdefault('_parts_' + p['greek'], []).append(c)

with open('data/morphology_reference.md') as f:
    morphology_ref = f.read()[:4000]

with open('data/pronunciation.csv') as f:
    pron_csv = f.read()

from src.data import ALL_LESSONS
from src.tts import extra_phrases, M, F

def get_word_data(gr):
    """Get all verified decomposition data for a word."""
    ctx = {}
    if gr in comp_map and isinstance(comp_map[gr], dict):
        c = comp_map[gr]
        ctx['compound'] = {
            'components': [{'greek': p['greek'], 'meaning': p['meaning_es']} for p in c['components']],
            'mnemonic': c['mnemonic_es']
        }
        if 'strongs_derivation' in c:
            ctx['strongs'] = c['strongs_derivation']
    parts_key = '_parts_' + gr
    if parts_key in comp_map:
        ctx['used_in'] = [{'word': c['lemma'], 'meaning': c['meaning_es']} for c in comp_map[parts_key][:3]]
    return ctx

def build_lesson_script(L, prev_vocab):
    """Generate the full text script of a lesson as the engine would produce it."""
    n = L['num']
    lines = []
    lines.append(f"=== INTRO ===")
    lines.append(f"[ES] {L['intro_es']}")
    for voice, text in L['dialogue']:
        tag = 'M' if voice == M else 'F'
        lines.append(f"[GR-{tag}] {text}")
    lines.append(f"[ES] {L['context_es']}")

    if prev_vocab:
        lines.append(f"\n=== REPASO ===")
        seen = set()
        unique = []
        for it in reversed(prev_vocab):
            if it['gr'] not in seen:
                seen.add(it['gr'])
                unique.append(it)
        random.seed(n); random.shuffle(unique)
        for it in unique[:6]:
            prompt = it['es'].rstrip('?.,;').split(',')[0]
            lines.append(f"[ES] ¿Cómo dirías {prompt}?")
            lines.append(f"[GR] {it['gr']}")

    lines.append(f"\n=== VOCABULARIO ===")
    for v in L['vocab']:
        lines.append(f"[ES] {v['note_es']}")
        lines.append(f"[GR] {v['gr']} (×2)")

    lines.append(f"\n=== FRASES ===")
    for p in L['phrases']:
        lines.append(f"[ES] {p['prompt_es']}")
        lines.append(f"[GR] {p['gr']} (×2)")

    lines.append(f"\n=== VERSÍCULO ===")
    v = L.get('verse', {})
    if v:
        lines.append(f"[ES] {v['ref_es']}")
        lines.append(f"[GR] {v['gr']}")
        lines.append(f"[ES] {v['explain_es']}")

    lines.append(f"\n=== CIERRE ===")
    lines.append(f"[ES] {L['closing_es']}")
    return '\n'.join(lines)

def get_prev_context(lesson_num):
    prev_lesson = None
    recent = []
    for L in ALL_LESSONS:
        if L['num'] == lesson_num: break
        if L['num'] == lesson_num - 1:
            prev_lesson = {
                'num': L['num'],
                'vocab': [f"{v['gr']} ({v['es']})" for v in L['vocab']],
                'phrases': [f"{p['gr']} ({p['es']})" for p in L['phrases'][:4]]
            }
        if L['num'] >= max(1, lesson_num - 5):
            recent.append(f"L{L['num']}: {', '.join(v['gr'] for v in L['vocab'][:4])}...")
    return prev_lesson, recent

def enrich_lesson(lesson_num):
    L = [l for l in ALL_LESSONS if l['num'] == lesson_num][0]
    prev_lesson, recent = get_prev_context(lesson_num)

    # Build prev_vocab for review section
    all_vocab = []
    for data in ALL_LESSONS:
        if data['num'] >= lesson_num: break
        for v in data['vocab']:
            all_vocab.append({'gr': v['gr'], 'es': v['es']})
        for p in data['phrases']:
            all_vocab.append({'gr': p['gr'], 'es': p['es']})

    script = build_lesson_script(L, all_vocab)

    # Gather word decomposition data
    word_data = {}
    for v in L['vocab']:
        d = get_word_data(v['gr'])
        if d: word_data[v['gr']] = d
    for p in L['phrases']:
        for w in p['gr'].split():
            d = get_word_data(w.rstrip('.,;?!'))
            if d: word_data[w.rstrip('.,;?!')] = d

    context = ""
    if prev_lesson:
        context += f"\nLECCIÓN ANTERIOR (L{prev_lesson['num']}):\n  Vocab: {', '.join(prev_lesson['vocab'])}\n  Frases: {', '.join(prev_lesson['phrases'])}\n"
    if recent:
        context += f"\nÚLTIMAS LECCIONES:\n  " + '\n  '.join(recent) + "\n"

    prompt = f"""Eres un profesor experto de griego koiné. Recibes el script automatizado de una lección de audio estilo Pimsleur y debes REESCRIBIRLO para que suene natural y educativo.

SCRIPT AUTOMATIZADO DE LA LECCIÓN {lesson_num}:
{script}

DATOS DE DESCOMPOSICIÓN DE PALABRAS (verificados):
{json.dumps(word_data, ensure_ascii=False, indent=2)}

REFERENCIA DE SUFIJOS Y PREFIJOS GRIEGOS:
{morphology_ref[:2000]}

PRONUNCIACIÓN (griego moderno, como suena en el TTS):
{pron_csv}

CONTEXTO:{context}

INSTRUCCIONES:
1. REESCRIBE cada [ES] para que suene natural, como un profesor real hablando.
2. DESGLOSA cada palabra de vocabulario en sus componentes (raíz, prefijo, sufijo) cuando sea posible. Usa SOLO los datos verificados de arriba. Si no hay datos, explica la palabra de forma clara sin inventar etimología.
3. DESGLOSA cada frase explicando cada palabra que la compone.
4. CORRIGE errores: si un prompt dice "¿Cómo dirías él, ella, ello?" pero el griego es solo αὐτός (masculino), corrígelo a "¿Cómo dirías él?".
5. Si una nota dice "Escucha la frase completa" pero solo se reproduce una palabra, quita esa promesa.
6. NO menciones cuántas veces aparece una palabra en el NT.
7. Máximo 3 oraciones por nota de vocabulario. Será leído por TTS.
8. Escribe números en letras. Sin abreviaciones.
9. Las notas de vocabulario terminan con "Escucha."
10. Si el alumno ya aprendió algo en lecciones anteriores, di "Ya conoces X".

FORMATO DE RESPUESTA — JSON exacto:
{{
  "vocab": [{{"gr": "...", "note_es": "..."}}],
  "phrases": [{{"gr": "...", "prompt_es": "..."}}],
  "review": [{{"gr": "...", "prompt_es": "..."}}],
  "verse_explain": "...",
  "closing": "..."
}}

SOLO el JSON, nada más."""

    response = bedrock.invoke_model(
        modelId=MODEL,
        body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': 12000,
            'messages': [{'role': 'user', 'content': prompt}]
        })
    )
    result = json.loads(response['body'].read())
    text = result['content'][0]['text']
    start = text.find('{')
    end = text.rfind('}') + 1
    return json.loads(text[start:end])

if __name__ == '__main__':
    targets = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [1]
    results = {}
    for n in targets:
        print(f'Enriching L{n}...', flush=True)
        enriched = enrich_lesson(n)
        results[n] = enriched
        for item in enriched.get('vocab', []):
            print(f'  V [{item["gr"]}] {item["note_es"][:80]}...')
        for item in enriched.get('phrases', []):
            print(f'  P [{item["gr"]}] {item["prompt_es"][:80]}...')
        if enriched.get('review'):
            print(f'  R [{len(enriched["review"])} review items]')
        print()

    os.makedirs('kiro-test', exist_ok=True)
    with open('kiro-test/enriched_notes.json', 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f'Saved {len(results)} lessons to kiro-test/enriched_notes.json')
