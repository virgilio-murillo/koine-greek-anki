"""Enrich lesson scripts — LLM modifies only ES text in the structured JSON."""
import json, boto3, sys, os
sys.path.insert(0, ".")

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
MODEL = 'us.anthropic.claude-sonnet-4-20250514-v1:0'

with open('data/matthew/compounds_enriched.json') as f:
    compounds = json.load(f)
with open('data/morphology_reference.md') as f:
    morphology_ref = f.read()[:3000]

comp_map = {}
for c in compounds:
    comp_map[c['lemma']] = c
    for p in c['components']:
        comp_map.setdefault('_parts_' + p['greek'], []).append(c)

from src.data import ALL_LESSONS

def get_word_data(lesson_num):
    L = [l for l in ALL_LESSONS if l['num'] == lesson_num][0]
    data = {}
    for v in L['vocab']:
        gr = v['gr']
        if gr in comp_map and isinstance(comp_map[gr], dict):
            c = comp_map[gr]
            data[gr] = {
                'components': [{'greek': p['greek'], 'meaning': p['meaning_es']} for p in c['components']],
                'mnemonic': c['mnemonic_es']
            }
        parts_key = '_parts_' + gr
        if parts_key in comp_map:
            data.setdefault(gr, {})['used_in'] = [
                {'word': c['lemma'], 'meaning': c['meaning_es']} for c in comp_map[parts_key][:3]
            ]
    return data

def get_prev_context(lesson_num):
    prev = None; recent = []
    for L in ALL_LESSONS:
        if L['num'] == lesson_num: break
        if L['num'] == lesson_num - 1:
            prev = f"L{L['num']}: {', '.join(v['gr']+'('+v['es']+')' for v in L['vocab'])}"
        if L['num'] >= max(1, lesson_num - 5):
            recent.append(f"L{L['num']}: {', '.join(v['gr'] for v in L['vocab'][:4])}...")
    return prev, recent

def enrich_script(script_path):
    with open(script_path) as f:
        script = json.load(f)
    lesson_num = script['lesson']
    word_data = get_word_data(lesson_num)
    prev, recent = get_prev_context(lesson_num)

    # Build readable version for LLM
    readable = []
    for i, seg in enumerate(script['segments']):
        if seg['lang'] == 'es':
            readable.append(f"[{i}] [ES] {seg['text']}")
        elif seg['lang'] == 'gr':
            readable.append(f"[{i}] [GR] {seg['text']}")
        # skip silences

    context = ""
    if prev: context += f"\nLección anterior: {prev}\n"
    if recent: context += f"Últimas lecciones: {'; '.join(recent)}\n"

    prompt = f"""Eres el editor de un curso de audio de griego koiné estilo Pimsleur.

Recibes el script de la lección {lesson_num} como una lista numerada de segmentos [ES] (español, narradora) y [GR] (griego, audio TTS). Los segmentos [GR] NO se pueden modificar. Solo puedes modificar el texto de los segmentos [ES].

SCRIPT:
{chr(10).join(readable)}

DATOS DE DESCOMPOSICIÓN DE PALABRAS (verificados):
{json.dumps(word_data, ensure_ascii=False, indent=2)}

REFERENCIA DE MORFOLOGÍA:
{morphology_ref[:2000]}

CONTEXTO:{context}

REGLAS:
- Solo modifica segmentos [ES]. Los [GR] son intocables.
- El alumno NO es lingüista pero SÍ quiere aprender los términos. SIEMPRE explica primero de forma simple, y LUEGO menciona el término técnico.
  MAL: "La terminación -ομαι indica voz media. Esto se llama verbo deponente."
  BIEN: "La terminación -ομαι significa que la acción la haces tú mismo. ἔρχομαι, yo vengo, yo mismo me muevo. Esto en gramática se llama voz media."
  MAL: "La terminación -ου es imperativo."
  BIEN: "Cuando cambias la terminación a -ου, conviertes el verbo en una orden. ἔρχου significa ven. A esto se le llama imperativo."
  MAL: "Es la forma dativa del pronombre."
  BIEN: "σοι es la forma que usas cuando le diriges algo a alguien, como en paz a ti. Esta forma se llama dativo."
- NUNCA digas "no te preocupes por eso". Si mencionas algo, explícalo de forma que cualquier persona lo entienda, y luego dale el nombre técnico.

VOCABULARIO (notas que terminan con "Escucha."):
- Explica qué significa la palabra. Máximo 4 oraciones.
- Si la palabra tiene PREFIJO conocido, explica en lenguaje simple: "Empieza con X que significa Y, así que la palabra completa significa Z."
- Si la palabra tiene SUFIJO o TERMINACIÓN conocida, explica qué hace de forma práctica con un ejemplo: "-σις es como -ción en español, indica una acción", "-τής es como -dor, indica quién hace algo".
- Si la palabra es COMPUESTA y hay datos en DESCOMPOSICIÓN, desglosa cada parte con un ejemplo cotidiano.
- Termina con "Escucha."

FRASES (prompts que terminan con "Di X" o "¿Cómo dirías X?"):
- Explica de qué palabras se compone y qué significa cada una.
- Si el orden es diferente al español, explícalo con un ejemplo simple.
- Termina con "Di X" o "¿Cómo dirías X?"

CORRECCIONES:
- Si dice "¿Cómo dirías él, ella, ello?" y el griego es αὐτός, corrígelo a "¿Cómo dirías él?"
- NO menciones frecuencia ni cuántas veces aparece en el NT.
- Si el alumno ya aprendió algo, di "Ya conoces X".
- Escribe números en letras. Sin abreviaciones.

RESPONDE con un JSON object donde las keys son los números de segmento y los values son el texto nuevo. Incluye TODOS los segmentos [ES], no solo los que cambies.
Ejemplo: {{"0": "texto", "5": "otro texto", "12": "más texto"}}
SOLO el JSON."""

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
    changes = json.loads(text[start:end])

    # Apply changes
    modified = 0
    for idx_str, new_text in changes.items():
        idx = int(idx_str)
        if idx < len(script['segments']) and script['segments'][idx]['lang'] == 'es':
            script['segments'][idx]['text'] = new_text
            modified += 1

    out_path = script_path.replace('_script.json', '_enriched.json')
    with open(out_path, 'w') as f:
        json.dump(script, f, ensure_ascii=False, indent=2)
    print(f"  L{lesson_num}: {modified} segments modified → {out_path}")
    return out_path

if __name__ == '__main__':
    paths = sys.argv[1:]
    for p in paths:
        enrich_script(p)
