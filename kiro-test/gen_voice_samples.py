"""Play one sample word from each Greek Wavenet voice."""
import os, time
from google.cloud import texttospeech
from pydub import AudioSegment
import unicodedata

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/.config/gcloud/koine-tts-key.json")
gtts = texttospeech.TextToSpeechClient()

OUT = "kiro-test/wavenet_test"
SAMPLE = "Εἰρήνη σοι"  # paz a ti - good test phrase

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

voices = ["el-GR-Wavenet-A","el-GR-Wavenet-B","el-GR-Wavenet-C","el-GR-Wavenet-D","el-GR-Wavenet-E"]
mono = to_mono(SAMPLE)
combined = AudioSegment.empty()

for v in voices:
    label = v.split("-")[-1]  # A, B, C, D, E
    print(f"  Generating {v}...", end=" ", flush=True)
    for attempt in range(5):
        try:
            r = gtts.synthesize_speech(
                input=texttospeech.SynthesisInput(text=mono),
                voice=texttospeech.VoiceSelectionParams(language_code="el-GR", name=v),
                audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=0.75))
            p = f"{OUT}/voice_{label}.mp3"
            with open(p, "wb") as f: f.write(r.audio_content)
            audio = AudioSegment.from_mp3(p)
            print(f"{len(audio)}ms")
            # 2s silence as separator between voices
            combined += AudioSegment.silent(1500) + audio
            break
        except Exception:
            wait = min(15, 5*(attempt+1)); print(f"retry {wait}s...", end=" ", flush=True); time.sleep(wait)

outfile = f"{OUT}/all_voices_sample.mp3"
combined.export(outfile, format="mp3")
print(f"\n✓ {outfile} ({len(combined)/1000:.1f}s)")
print("Orden: A → B → C → D → E (1.5s silencio entre cada una)")
