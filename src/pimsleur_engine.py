"""Full Pimsleur engine: compact lesson data → full lesson with proper GIR cycling."""
import boto3, os, unicodedata, hashlib, random
from google.cloud import texttospeech
from pydub import AudioSegment

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/.config/gcloud/koine-tts-key.json")

_polly = None
_gtts = None
def get_polly():
    global _polly
    if not _polly: _polly = boto3.client("polly", region_name="us-east-1")
    return _polly
def get_gtts():
    global _gtts
    if not _gtts: _gtts = texttospeech.TextToSpeechClient()
    return _gtts

CACHE = "/tmp/tts_cache"
os.makedirs(CACHE, exist_ok=True)
M = "el-GR-Chirp3-HD-Charon"
F = "el-GR-Chirp3-HD-Kore"

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

def _cp(pfx, txt, v, ex=""):
    h = hashlib.md5(f"{txt}_{v}_{ex}".encode()).hexdigest()[:12]
    return os.path.join(CACHE, f"{pfx}_{h}.mp3")

def es(text, voice="Mia", engine="neural"):
    p = _cp("es", text, voice, engine)
    if not os.path.exists(p):
        r = get_polly().synthesize_speech(Text=text, OutputFormat="mp3", VoiceId=voice, Engine=engine, LanguageCode="es-MX")
        with open(p,"wb") as f: f.write(r["AudioStream"].read())
    return AudioSegment.from_mp3(p)

def gr(text, voice=F, speed=0.75):
    mono = to_mono(text)
    p = _cp("gr2", mono, voice, str(speed))
    if not os.path.exists(p):
        # Try primary voice (Chirp3-HD)
        r = get_gtts().synthesize_speech(
            input=texttospeech.SynthesisInput(text=mono),
            voice=texttospeech.VoiceSelectionParams(language_code="el-GR", name=voice),
            audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=speed))
        with open(p,"wb") as f: f.write(r.audio_content)
        # Check if audio is too short (TTS failure on short words)
        audio = AudioSegment.from_mp3(p)
        if len(audio) < 400 and len(mono.strip()) > 0:
            # Fallback to Wavenet-B which handles short words
            fb_voice = "el-GR-Wavenet-B" if "Kore" in voice else "el-GR-Wavenet-B"
            r = get_gtts().synthesize_speech(
                input=texttospeech.SynthesisInput(text=mono),
                voice=texttospeech.VoiceSelectionParams(language_code="el-GR", name=fb_voice),
                audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=speed))
            with open(p,"wb") as f: f.write(r.audio_content)
    return AudioSegment.from_mp3(p)

P = AudioSegment.silent

def spd(n):
    return 0.75 if n <= 7 else (0.85 if n <= 15 else 1.0)

def build(data, prev_vocab=None):
    """Generate full Pimsleur lesson from structured data.
    data keys: num, intro_es, dialogue[(voice,gr)], context_es,
               vocab[{gr,es,note_es,voice?}], phrases[{gr,es,prompt_es}],
               recon[{prompt_es,answer_gr,answer_voice?,other_gr?,other_voice?}],
               verse{gr,ref_es,explain_es,voice?}, closing_es
    """
    n = data["num"]; s = spd(n); prev = prev_vocab or []
    L = AudioSegment.empty()
    
    # 1. INTRO + DIALOGUE
    L += es(data["intro_es"]) + P(800)
    for v, t in data["dialogue"]:
        L += gr(t, voice=v, speed=s) + P(400)
    L += P(600) + es(data["context_es"]) + P(800)
    
    # 2. REVIEW PREVIOUS
    if prev:
        L += es("Antes de aprender palabras nuevas, repasemos.") + P(500)
        random.seed(n); items = list(prev[-8:]); random.shuffle(items)
        for it in items[:6]:
            L += es(f"¿Cómo dirías {it['es']}?") + P(4000) + gr(it["gr"], speed=s) + P(500)
        L += P(300)
    
    # 3. NEW VOCABULARY — with interleaved GIR
    vocab = data["vocab"]
    for i, w in enumerate(vocab):
        vo = w.get("voice", F)
        L += es(w["note_es"]) + P(300)
        L += gr(w["gr"], voice=vo, speed=s) + P(3500)
        L += gr(w["gr"], voice=vo, speed=s) + P(800)
        if len(w["gr"]) > 8:  # back-chain long words
            L += es("Escucha una vez más.") + P(300)
            L += gr(w["gr"], voice=vo, speed=s) + P(3500) + gr(w["gr"], voice=vo, speed=s) + P(800)
        # GIR: recall previous new word (~25s interval)
        if i > 0:
            pv = vocab[i-1]
            L += es(f"¿Cómo dirías {pv['es']}?") + P(4000) + gr(pv["gr"], speed=s) + P(500)
        # GIR: recall word from 2 ago (~2min interval)
        if i > 2:
            pv2 = vocab[i-3]
            L += es(f"¿Cómo dirías {pv2['es']}?") + P(4000) + gr(pv2["gr"], speed=s) + P(500)
    
    # 4. PHRASE BUILDING + GIR
    phrases = data["phrases"]
    for i, ph in enumerate(phrases):
        L += es(ph["prompt_es"]) + P(300)
        L += gr(ph["gr"], speed=s) + P(4000)
        L += gr(ph["gr"], speed=s) + P(800)
        # GIR: recall vocab
        if i < len(vocab):
            v = vocab[i]
            L += es(f"¿Cómo dirías {v['es']}?") + P(4000) + gr(v["gr"], speed=s) + P(500)
        # GIR: recall earlier phrase (~2min)
        if i > 1:
            op = phrases[i-2]
            L += es(f"¿Cómo dirías {op['es']}?") + P(4500) + gr(op["gr"], speed=s) + P(500)
    
    # 5. GIR CYCLE 2 — all vocab + phrases shuffled
    L += es("Practiquemos todo junto.") + P(500)
    all_it = [(v["es"], v["gr"]) for v in vocab] + [(p["es"], p["gr"]) for p in phrases]
    if prev: all_it += [(pv["es"], pv["gr"]) for pv in prev[-4:]]
    random.shuffle(all_it)
    for e, g in all_it:
        L += es(f"¿Cómo dirías {e}?") + P(4500) + gr(g, speed=s) + P(500)
    L += P(300)
    
    # 6. DIALOGUE RECONSTRUCTION
    recon = data.get("recon", [])
    if recon:
        L += es("Ahora reconstruyamos la conversación. Tú participas.") + P(800)
        for r in recon:
            if r.get("other_gr"):
                L += gr(r["other_gr"], voice=r.get("other_voice", M), speed=s) + P(500)
            L += es(r["prompt_es"]) + P(5000)
            L += gr(r["answer_gr"], voice=r.get("answer_voice", F), speed=s) + P(600)
    
    # 7. GIR CYCLE 3 — rapid fire all new items
    L += es("Repaso rápido.") + P(400)
    final = [(v["es"], v["gr"]) for v in vocab] + [(p["es"], p["gr"]) for p in phrases[:5]]
    for e, g in final:
        L += es(e + ".") + P(3500) + gr(g, speed=s) + P(400)
    
    # 8. VERSE + CLOSING
    v = data.get("verse", {})
    if v:
        L += P(300) + es(v["ref_es"]) + P(500)
        L += gr(v["gr"], voice=v.get("voice", M), speed=s) + P(600)
        L += es(v["explain_es"]) + P(800)
    L += es(data["closing_es"]) + P(500)
    
    # Export
    os.makedirs("decks/lessons", exist_ok=True)
    path = f"decks/lessons/lesson_{n:02d}.mp3"
    L.export(path, format="mp3")
    dur = len(L)/1000
    print(f"  ✓ Lesson {n}: {path} ({dur:.0f}s = {dur/60:.1f} min)")
    return path
