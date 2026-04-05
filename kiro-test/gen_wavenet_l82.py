"""Generate all L82 Greek words using el-GR-Wavenet-B for quality check."""
import os, time, unicodedata, hashlib
from google.cloud import texttospeech
from pydub import AudioSegment
import boto3

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/.config/gcloud/koine-tts-key.json")
gtts = texttospeech.TextToSpeechClient()
polly = boto3.client("polly", region_name="us-east-1")

OUT = "kiro-test/wavenet_test"
os.makedirs(OUT, exist_ok=True)
VOICE = "el-GR-Wavenet-B"
SPEED = 0.75

import sys; sys.path.insert(0, ".")
from src.lesson_data_81_85 import L82
WORDS = [(v["gr"], v["es"]) for v in L82["vocab"]] + [(p["gr"], p["es"]) for p in L82["phrases"]]

def to_mono(text):
    r = []
    for c in unicodedata.normalize('NFD', text):
        cat = unicodedata.category(c)
        nm = unicodedata.name(c, '')
        if cat.startswith('L') or cat in ('Zs','Po','Ps','Pe','Pd','Nd'):
            r.append(c)
        elif 'OXIA' in nm or 'TONOS' in nm or 'ACUTE' in nm:
            r.append('\u0301')
    return unicodedata.normalize('NFC', ''.join(r))

def gen_gr(text, outpath):
    if os.path.exists(outpath): return AudioSegment.from_mp3(outpath)
    mono = to_mono(text)
    for attempt in range(8):
        try:
            r = gtts.synthesize_speech(
                input=texttospeech.SynthesisInput(text=mono),
                voice=texttospeech.VoiceSelectionParams(language_code="el-GR", name=VOICE),
                audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=SPEED))
            with open(outpath, "wb") as f: f.write(r.audio_content)
            return AudioSegment.from_mp3(outpath)
        except Exception:
            wait = min(15, 5*(attempt+1)); print(f"retry in {wait}s...", end=" ", flush=True); time.sleep(wait)
    raise RuntimeError(f"Failed: {text}")

def gen_es(text):
    h = hashlib.md5(text.encode()).hexdigest()[:8]
    p = f"{OUT}/_label_{h}.mp3"
    if not os.path.exists(p):
        r = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId="Mia", Engine="neural", LanguageCode="es-MX")
        with open(p, "wb") as f: f.write(r["AudioStream"].read())
    return AudioSegment.from_mp3(p)

P = AudioSegment.silent
combined = AudioSegment.empty()
for i, (gr_text, es_text) in enumerate(WORDS):
    fname = f"l82_{i+1:02d}.mp3"
    fpath = f"{OUT}/{fname}"
    print(f"  [{i+1}/{len(WORDS)}] {gr_text} ({es_text})...", end=" ", flush=True)
    audio = gen_gr(gr_text, fpath)
    print(f"{len(audio)}ms")
    combined += gen_es(f"{es_text}.") + P(300) + audio + P(500) + audio + P(1000)

outfile = f"{OUT}/all_l82_wavenet_b.mp3"
combined.export(outfile, format="mp3")
print(f"\n✓ Combined: {outfile} ({len(combined)/1000:.1f}s)")
