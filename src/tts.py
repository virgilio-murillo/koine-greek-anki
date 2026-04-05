"""TTS module — single source of truth for all voice synthesis."""
import boto3, os, io, re, unicodedata, hashlib
from google.cloud import texttospeech
from pydub import AudioSegment

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/.config/gcloud/koine-tts-key.json")

# --- Voices ---
M = "el-GR-Chirp3-HD-Achird"
F = "el-GR-Wavenet-B"
FALLBACK_M = ["el-GR-Chirp3-HD-Charon", "el-GR-Chirp3-HD-Orus", "el-GR-Chirp3-HD-Puck", "el-GR-Wavenet-B"]
FALLBACK_F = ["el-GR-Chirp3-HD-Kore", "el-GR-Chirp3-HD-Achernar", "el-GR-Chirp3-HD-Aoede", "el-GR-Chirp3-HD-Achird"]

# --- Cache ---
CACHE = "/tmp/tts_cache"
os.makedirs(CACHE, exist_ok=True)
QA_REPORT = os.path.join(CACHE, "tts_qa_report.txt")

# --- Clients (lazy) ---
_polly = None
_gtts = None
def _get_polly():
    global _polly
    if not _polly: _polly = boto3.client("polly", region_name="us-east-1")
    return _polly
def _get_gtts():
    global _gtts
    if not _gtts: _gtts = texttospeech.TextToSpeechClient()
    return _gtts

# --- Helpers ---
def to_mono(text):
    """Convert polytonic Greek to monotonic for TTS compatibility."""
    r = []
    for c in unicodedata.normalize('NFD', text):
        cat = unicodedata.category(c)
        nm = unicodedata.name(c, '')
        if cat.startswith('L') or cat in ('Zs','Po','Ps','Pe','Pd','Nd'):
            r.append(c)
        elif 'OXIA' in nm or 'TONOS' in nm or 'ACUTE' in nm:
            r.append('\u0301')
    return unicodedata.normalize('NFC', ''.join(r))

def _greek_len(text):
    return sum(1 for c in text if '\u0370' <= c <= '\u03FF' or '\u1F00' <= c <= '\u1FFF')

def _min_dur(text):
    n = _greek_len(text)
    return max(400, min(n, 4) * 150 + max(0, n - 4) * 80)

def _cache_path(pfx, txt, v, ex=""):
    h = hashlib.md5(f"{txt}_{v}_{ex}".encode()).hexdigest()[:12]
    return os.path.join(CACHE, f"{pfx}_{h}.mp3")

def _synth(mono, voice, speed):
    r = _get_gtts().synthesize_speech(
        input=texttospeech.SynthesisInput(text=mono),
        voice=texttospeech.VoiceSelectionParams(language_code="el-GR", name=voice),
        audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=speed))
    data = r.audio_content
    dur = len(AudioSegment.from_mp3(io.BytesIO(data)))
    return data, dur

# --- Public API ---
def es(text, voice="Mia", engine="neural"):
    """Synthesize Spanish text via AWS Polly."""
    p = _cache_path("es", text, voice, engine)
    if not os.path.exists(p):
        r = _get_polly().synthesize_speech(Text=text, OutputFormat="mp3", VoiceId=voice, Engine=engine, LanguageCode="es-MX")
        with open(p,"wb") as f: f.write(r["AudioStream"].read())
    return AudioSegment.from_mp3(p)

def gr(text, voice=None, speed=0.75):
    """Synthesize Greek text via Google TTS with smart fallback."""
    if voice is None: voice = F
    mono = to_mono(text)
    p = _cache_path("gr3", mono, voice, str(speed))
    if os.path.exists(p):
        return AudioSegment.from_mp3(p)
    md = _min_dur(mono)
    best, best_dur = None, 0
    # 1) Retry primary voice 3x
    for _ in range(3):
        try:
            data, dur = _synth(mono, voice, speed)
        except Exception:
            continue
        if dur >= md:
            with open(p,"wb") as f: f.write(data)
            return AudioSegment.from_mp3(p)
        if dur > best_dur: best, best_dur = data, dur
    # 2) Try 4 fallback voices
    fallbacks = FALLBACK_M if voice == M else FALLBACK_F
    for fb in fallbacks:
        if fb == voice: continue
        try:
            data, dur = _synth(mono, fb, speed)
        except Exception:
            continue
        if dur >= md:
            with open(p,"wb") as f: f.write(data)
            return AudioSegment.from_mp3(p)
        if dur > best_dur: best, best_dur = data, dur
    # 3) Nothing passed — log and use best
    with open(QA_REPORT, "a") as f:
        f.write(f"SHORT: '{text}' voice={voice} best={best_dur}ms min={md}ms\n")
    print(f"  ⚠️ QA: '{text}' best={best_dur}ms < min={md}ms")
    with open(p,"wb") as f: f.write(best)
    return AudioSegment.from_mp3(p)

# --- Note phrase extraction ---
_GR_PHRASE = re.compile(r'[\u0370-\u03FF\u1F00-\u1FFF][\u0370-\u03FF\u1F00-\u1FFF\u0300-\u036F\s\u0027\u1FBD]+')

def extra_phrases(note, gr_word):
    """Extract Greek phrases from a Spanish note that are longer than the vocab word."""
    found = []
    for m in _GR_PHRASE.findall(note):
        phrase = m.strip()
        if len(phrase) > len(gr_word) and gr_word.lower().rstrip(';.,') in phrase.lower():
            if phrase not in found:
                found.append(phrase)
    return found

P = AudioSegment.silent
