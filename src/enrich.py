"""Enrich lesson data with etymology, pronunciation, and previous lesson context.
Code extracts verified facts — LLM only writes prose from them."""
import json, csv, boto3, copy, sys, os
sys.path.insert(0, ".")

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
MODEL = 'us.anthropic.claude-sonnet-4-20250514-v1:0'

# --- Load reference data ---
with open('data/matthew/compounds_enriched.json') as f:
    compounds = json.load(f)
with open('data/nt_top600.json') as f:
    freq = {w['lemma']: w['count'] for w in json.load(f)}

comp_map = {}
for c in compounds:
    comp_map[c['lemma']] = c
    for p in c['components']:
        comp_map.setdefault('_parts_' + p['greek'], []).append(c)

# Load pronunciation
pron_map = {}  # greek text -> pronunciation info
with open('data/pronunciation.csv') as f:
    for row in csv.DictReader(f):
        key = row.get('letter') or row.get('diphthong') or row.get('combination') or row.get('confusing_pair', '')
        if key:
            pron_map[key] = row

from src.data import ALL_LESSONS

def get_pronunciation_notes(text):
    """Find relevant pronunciation warnings for a Greek text."""
    notes = []
    for key, info in pron_map.items():
        if key in text and info.get('sounds_like_es'):
            notes.append(f"{key} suena como '{info['sounds_like_es']}'" +
                        (f" ({info['notes']})" if info.get('notes') else ""))
    return notes

def get_word_facts(gr):
    ctx = {}
    if gr in comp_map and isinstance(comp_map[gr], dict):
        c = comp_map[gr]
        ctx['es_compound_de'] = ' + '.join(f'{p["greek"]} ({p["meaning_es"]})' for p in c['components'])
        ctx['mnemonic'] = c['mnemonic_es']
    if gr in freq:
        ctx['frecuencia_nt'] = freq[gr]
    parts_key = '_parts_' + gr
    if parts_key in comp_map:
        ctx['componente_de'] = [f'{c["lemma"]} ({c["meaning_es"]})' for c in comp_map[parts_key][:3]]
    pron = get_pronunciation_notes(gr)
    if pron:
        ctx['pronunciacion'] = pron
    return ctx

def get_prev_context(lesson_num):
    """Build context from previous lessons."""
    prev_lesson = None
    recent_summary = []
    for L in ALL_LESSONS:
        if L['num'] == lesson_num:
            break
        if L['num'] == lesson_num - 1:
            prev_lesson = {
                'num': L['num'],
                'vocab': [f"{v['gr']} ({v['es']})" for v in L['vocab']],
                'phrases': [f"{p['gr']} ({p['es']})" for p in L['phrases']]
            }
        if L['num'] >= max(1, lesson_num - 5):
            recent_summary.append(f"L{L['num']}: {', '.join(v['gr'] for v in L['vocab'][:4])}...")
    return prev_lesson, recent_summary

def enrich_lesson(lesson_num):
    L = [l for l in ALL_LESSONS if l['num'] == lesson_num][0]
    prev_lesson, recent_summary = get_prev_context(lesson_num)

    vocab_with_facts = []
    for v in L['vocab']:
        facts = get_word_facts(v['gr'])
        vocab_with_facts.append({
            'gr': v['gr'], 'es': v['es'],
            'current_note': v['note_es'],
            'verified_facts': facts
        })

    phrases_with_facts = []
    for p in L['phrases']:
        words = p['gr'].split()
        breakdown = []
        for w in words:
            clean = w.lower().rstrip('.,;?!')
            for v in L['vocab']:
                if v['gr'].lower().rstrip('.,;?!') == clean:
                    breakdown.append(f'{w} = {v["es"]}')
                    break
            else:
                breakdown.append(w)
        pron = get_pronunciation_notes(p['gr'])
        phrases_with_facts.append({
            'gr': p['gr'], 'es': p['es'],
            'current_prompt': p['prompt_es'],
            'word_breakdown': breakdown,
            'num_words': len(words),
            'pronunciation_notes': pron
        })

    context_block = ""
    if prev_lesson:
        context_block += f"\nLECCIÓN ANTERIOR (L{prev_lesson['num']}):\n"
        context_block += f"  Vocab: {', '.join(prev_lesson['vocab'])}\n"
        context_block += f"  Frases: {', '.join(prev_lesson['phrases'][:4])}\n"
    if recent_summary:
        context_block += f"\nRESUMEN LECCIONES RECIENTES:\n  " + '\n  '.join(recent_summary) + "\n"

    prompt = (
        "Eres un profesor de griego koiné creando lecciones de audio estilo Pimsleur en español.\n\n"
        "REGLAS ESTRICTAS:\n"
        "- Usa ÚNICAMENTE los datos proporcionados. NO inventes conexiones etimológicas.\n"
        "- Máximo 3 oraciones por nota/prompt. Será leído por TTS.\n"
        "- Estilo conversacional, como profesor hablando.\n"
        "- Escribe números en letras. Sin abreviaciones.\n"
        "- Si hay 'pronunciation_notes', SIEMPRE menciona cómo suena la frase.\n"
        "- Si el alumno ya aprendió una palabra en lecciones anteriores, di 'Ya conoces X'.\n\n"
        "PARTE 1 — VOCABULARIO (note_es):\n"
        "- Si 'verified_facts' está vacío, mejora solo el estilo.\n"
        "- Si hay 'componente_de', menciona SOLO las palabras listadas.\n"
        "- Si hay 'pronunciacion', menciona cómo suena.\n"
        "- Termina siempre con 'Escucha.'\n\n"
        f"{json.dumps(vocab_with_facts, ensure_ascii=False, indent=2)}\n\n"
        "PARTE 2 — FRASES (prompt_es):\n"
        "- Para frases de dos o más palabras, SIEMPRE explica el significado de CADA palabra usando word_breakdown.\n"
        "- Si hay 'pronunciation_notes', SIEMPRE advierte cómo suena y que son palabras separadas.\n"
        "- Ejemplo: 'σὺ εἶ se compone de σὺ que significa tú, y εἶ que significa eres. Suenan juntas como si, pero son dos palabras. ¿Cómo dirías tú eres?'\n"
        "- Termina con la pregunta o instrucción original.\n\n"
        f"{json.dumps(phrases_with_facts, ensure_ascii=False, indent=2)}\n\n"
        f"CONTEXTO DE LECCIONES ANTERIORES:{context_block}\n\n"
        'Responde con JSON: {"vocab": [{"gr":"...","note_es":"..."}], "phrases": [{"gr":"...","prompt_es":"..."}]}\n'
        "SOLO el JSON, nada más."
    )

    response = bedrock.invoke_model(
        modelId=MODEL,
        body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': 8000,
            'messages': [{'role': 'user', 'content': prompt}]
        })
    )
    result = json.loads(response['body'].read())
    text = result['content'][0]['text']
    start = text.find('{')
    end = text.rfind('}') + 1
    return json.loads(text[start:end])

if __name__ == '__main__':
    targets = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [1, 3, 30]
    results = {}
    for n in targets:
        print(f'Enriching L{n}...', flush=True)
        enriched = enrich_lesson(n)
        results[n] = enriched
        for item in enriched['vocab']:
            print(f'  V [{item["gr"]}] {item["note_es"][:90]}...')
        for item in enriched['phrases']:
            print(f'  P [{item["gr"]}] {item["prompt_es"][:90]}...')
        print()

    os.makedirs('kiro-test', exist_ok=True)
    with open('kiro-test/enriched_notes.json', 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f'Saved {len(results)} lessons to kiro-test/enriched_notes.json')
