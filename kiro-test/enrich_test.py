"""Enrich lesson vocab notes using LLM + compound/frequency data.
LLM only generates text — code extracts structured data from it."""
import json, boto3, sys
sys.path.insert(0, ".")

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
MODEL = 'us.anthropic.claude-sonnet-4-20250514-v1:0'

# Load enrichment data
with open('data/matthew/compounds_enriched.json') as f:
    compounds = json.load(f)
with open('data/nt_top600.json') as f:
    freq = {w['lemma']: w['count'] for w in json.load(f)}

# Build lookups
comp_map = {}
for c in compounds:
    comp_map[c['lemma']] = c
    for p in c['components']:
        comp_map.setdefault('_parts_' + p['greek'], []).append(c)

from src.data import ALL_LESSONS

def get_enrichment_context(gr):
    """Code-driven: extract ONLY verified data for a word."""
    ctx = {}
    if gr in comp_map and isinstance(comp_map[gr], dict):
        c = comp_map[gr]
        ctx['es_compound_de'] = ' + '.join(
            f'{p["greek"]} ({p["meaning_es"]})' for p in c['components']
        )
        ctx['mnemonic'] = c['mnemonic_es']
    if gr in freq:
        ctx['frecuencia_nt'] = freq[gr]
    parts_key = '_parts_' + gr
    if parts_key in comp_map:
        ctx['componente_de'] = [
            f'{c["lemma"]} ({c["meaning_es"]})'
            for c in comp_map[parts_key][:3]
        ]
    return ctx

results = {}
for lesson_num in [3, 30]:
    L = [l for l in ALL_LESSONS if l['num'] == lesson_num][0]

    # Code builds the verified facts per word
    vocab_with_facts = []
    for v in L['vocab']:
        facts = get_enrichment_context(v['gr'])
        vocab_with_facts.append({
            'gr': v['gr'],
            'es': v['es'],
            'current_note': v['note_es'],
            'verified_facts': facts
        })

    prompt = (
        "Eres un profesor de griego koiné creando notas de audio en español para un curso estilo Pimsleur.\n\n"
        "REGLAS ESTRICTAS:\n"
        "- Usa ÚNICAMENTE los datos en 'verified_facts' para enriquecer. NO inventes conexiones etimológicas.\n"
        "- Si 'verified_facts' está vacío, mejora solo el estilo y claridad de la nota actual.\n"
        "- Si hay 'componente_de', menciona SOLO las palabras listadas ahí, no otras.\n"
        "- Si hay 'es_compound_de', explica los componentes exactos listados.\n"
        "- Máximo 3 oraciones. Será leído por TTS.\n"
        "- Estilo conversacional, como profesor hablando.\n"
        "- Termina siempre con 'Escucha.'\n"
        "- Escribe números en letras. Sin abreviaciones.\n\n"
        f"Vocabulario de lección {lesson_num}:\n"
        f"{json.dumps(vocab_with_facts, ensure_ascii=False, indent=2)}\n\n"
        "Responde con un JSON array: [{\"gr\":\"...\",\"note_es\":\"...\"}]\n"
        "SOLO el JSON, nada más."
    )

    print(f'Enriching L{lesson_num}...', flush=True)
    response = bedrock.invoke_model(
        modelId=MODEL,
        body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': 4000,
            'messages': [{'role': 'user', 'content': prompt}]
        })
    )
    result = json.loads(response['body'].read())
    text = result['content'][0]['text']
    start = text.find('[')
    end = text.rfind(']') + 1
    enriched = json.loads(text[start:end])
    results[lesson_num] = enriched

    for item in enriched:
        print(f'  [{item["gr"]}]')
        print(f'  {item["note_es"]}')
        print()

with open('kiro-test/enriched_notes.json', 'w') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print('Saved to kiro-test/enriched_notes.json')
