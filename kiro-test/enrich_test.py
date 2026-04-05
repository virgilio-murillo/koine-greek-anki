"""Enrich lesson vocab + phrases using LLM + compound/frequency data.
LLM only generates text — code extracts verified data for it."""
import json, boto3, sys
sys.path.insert(0, ".")

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
MODEL = 'us.anthropic.claude-sonnet-4-20250514-v1:0'

with open('data/matthew/compounds_enriched.json') as f:
    compounds = json.load(f)
with open('data/nt_top600.json') as f:
    freq = {w['lemma']: w['count'] for w in json.load(f)}

comp_map = {}
for c in compounds:
    comp_map[c['lemma']] = c
    for p in c['components']:
        comp_map.setdefault('_parts_' + p['greek'], []).append(c)

from src.data import ALL_LESSONS

def get_enrichment_context(gr):
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
    return ctx

results = {}
for lesson_num in [1, 3, 30]:
    L = [l for l in ALL_LESSONS if l['num'] == lesson_num][0]

    vocab_with_facts = []
    for v in L['vocab']:
        facts = get_enrichment_context(v['gr'])
        vocab_with_facts.append({
            'gr': v['gr'], 'es': v['es'],
            'current_note': v['note_es'],
            'verified_facts': facts
        })

    # Build word breakdown for phrases
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
        phrases_with_facts.append({
            'gr': p['gr'], 'es': p['es'],
            'current_prompt': p['prompt_es'],
            'word_breakdown': breakdown,
            'num_words': len(words)
        })

    prompt = (
        "Eres un profesor de griego koiné creando lecciones de audio estilo Pimsleur en español.\n\n"
        "REGLAS ESTRICTAS:\n"
        "- Usa ÚNICAMENTE los datos proporcionados. NO inventes conexiones etimológicas.\n"
        "- Máximo 3 oraciones por nota/prompt. Será leído por TTS.\n"
        "- Estilo conversacional, como profesor hablando.\n"
        "- Escribe números en letras. Sin abreviaciones.\n\n"
        "PARTE 1 — VOCABULARIO (note_es):\n"
        "- Si 'verified_facts' está vacío, mejora solo el estilo.\n"
        "- Si hay 'componente_de', menciona SOLO las palabras listadas.\n"
        "- Termina siempre con 'Escucha.'\n\n"
        f"{json.dumps(vocab_with_facts, ensure_ascii=False, indent=2)}\n\n"
        "PARTE 2 — FRASES (prompt_es):\n"
        "- Para frases de dos o más palabras, SIEMPRE explica el significado de CADA palabra usando word_breakdown.\n"
        "- Si la pronunciación puede confundir (ej: σὺ εἶ suena como 'si' pero son dos palabras), SIEMPRE advierte cómo suena y aclara que son palabras separadas.\n"
        "- Formato: primero el desglose con significados, luego la pregunta/instrucción.\n"
        "- Ejemplo bueno: 'σὺ εἶ se compone de σὺ que significa tú, y εἶ que significa eres. Suenan juntas como si, pero son dos palabras. ¿Cómo dirías tú eres?'\n"
        "- Termina con la pregunta o instrucción original.\n\n"
        f"{json.dumps(phrases_with_facts, ensure_ascii=False, indent=2)}\n\n"
        'Responde con JSON: {"vocab": [{"gr":"...","note_es":"..."}], "phrases": [{"gr":"...","prompt_es":"..."}]}\n'
        "SOLO el JSON, nada más."
    )

    print(f'Enriching L{lesson_num}...', flush=True)
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
    enriched = json.loads(text[start:end])
    results[lesson_num] = enriched

    print(f'  VOCAB:')
    for item in enriched['vocab']:
        print(f'    [{item["gr"]}] {item["note_es"][:100]}...')
    print(f'  PHRASES:')
    for item in enriched['phrases']:
        print(f'    [{item["gr"]}] {item["prompt_es"][:100]}...')
    print()

with open('kiro-test/enriched_notes.json', 'w') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print('Saved to kiro-test/enriched_notes.json')
