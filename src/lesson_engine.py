"""Pimsleur Koine Greek lesson engine. Takes structured lesson data and generates audio."""
import boto3, os, unicodedata, hashlib, json
from google.cloud import texttospeech
from pydub import AudioSegment

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/.config/gcloud/koine-tts-key.json")

_polly = None
_gtts = None

def get_polly():
    global _polly
    if _polly is None:
        _polly = boto3.client("polly", region_name="us-east-1")
    return _polly

def get_gtts():
    global _gtts
    if _gtts is None:
        _gtts = texttospeech.TextToSpeechClient()
    return _gtts

CACHE_DIR = "/tmp/tts_cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def to_monotonic(text):
    result = []
    for char in unicodedata.normalize('NFD', text):
        cat = unicodedata.category(char)
        name = unicodedata.name(char, '')
        if cat.startswith('L') or cat in ('Zs', 'Po', 'Ps', 'Pe', 'Pd', 'Nd'):
            result.append(char)
        elif 'OXIA' in name or 'TONOS' in name or 'ACUTE' in name:
            result.append('\u0301')
    return unicodedata.normalize('NFC', ''.join(result))

def _cache_path(prefix, text, voice, extra=""):
    h = hashlib.md5(f"{text}_{voice}_{extra}".encode()).hexdigest()[:12]
    return os.path.join(CACHE_DIR, f"{prefix}_{h}.mp3")

def es(text, voice="Mia", engine="neural"):
    path = _cache_path("es", text, voice, engine)
    if not os.path.exists(path):
        resp = get_polly().synthesize_speech(Text=text, OutputFormat="mp3", VoiceId=voice, Engine=engine, LanguageCode="es-MX")
        with open(path, "wb") as f:
            f.write(resp["AudioStream"].read())
    return AudioSegment.from_mp3(path)

def gr(text, voice="el-GR-Chirp3-HD-Kore", speed=0.75):
    mono = to_monotonic(text)
    path = _cache_path("gr", mono, voice, str(speed))
    if not os.path.exists(path):
        resp = get_gtts().synthesize_speech(
            input=texttospeech.SynthesisInput(text=mono),
            voice=texttospeech.VoiceSelectionParams(language_code="el-GR", name=voice),
            audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=speed)
        )
        with open(path, "wb") as f:
            f.write(resp.audio_content)
    return AudioSegment.from_mp3(path)

P = AudioSegment.silent
M = "el-GR-Chirp3-HD-Charon"  # male
F = "el-GR-Chirp3-HD-Kore"    # female

def build_lesson(segments, lesson_num, output_dir="decks/lessons"):
    """Build a lesson from a list of audio segments."""
    os.makedirs(output_dir, exist_ok=True)
    lesson = AudioSegment.empty()
    for seg in segments:
        lesson += seg
    path = os.path.join(output_dir, f"lesson_{lesson_num:02d}.mp3")
    lesson.export(path, format="mp3")
    duration = len(lesson) / 1000
    print(f"  ✓ Lesson {lesson_num}: {path} ({duration:.0f}s = {duration/60:.1f} min)")
    return path
