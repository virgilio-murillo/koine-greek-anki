"""Generate a 5-minute Pimsleur-style test lesson for Koine Greek."""
import boto3, json, os, unicodedata, tempfile
from google.cloud import texttospeech
from pydub import AudioSegment

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/.config/gcloud/koine-tts-key.json")

# Clients
polly = boto3.client("polly", region_name="us-east-1")
gtts = texttospeech.TextToSpeechClient()

# Cache
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

def spanish(text, voice="Mia", engine="neural"):
    """Generate Spanish narration via Polly."""
    key = f"es_{voice}_{hash(text)}.mp3"
    path = os.path.join(CACHE_DIR, key)
    if not os.path.exists(path):
        resp = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId=voice, Engine=engine, LanguageCode="es-MX")
        with open(path, "wb") as f:
            f.write(resp["AudioStream"].read())
    return AudioSegment.from_mp3(path)

def greek(text, voice="el-GR-Chirp3-HD-Kore", speed=0.75):
    """Generate Greek speech via Google Cloud TTS."""
    mono = to_monotonic(text)
    key = f"gr_{voice}_{speed}_{hash(mono)}.mp3"
    path = os.path.join(CACHE_DIR, key)
    if not os.path.exists(path):
        resp = gtts.synthesize_speech(
            input=texttospeech.SynthesisInput(text=mono),
            voice=texttospeech.VoiceSelectionParams(language_code="el-GR", name=voice),
            audio_config=texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                speaking_rate=speed
            )
        )
        with open(path, "wb") as f:
            f.write(resp.audio_content)
    return AudioSegment.from_mp3(path)

def pause(ms):
    return AudioSegment.silent(duration=ms)

# === BUILD THE 5-MINUTE TEST ===
print("Generating audio segments...")
lesson = AudioSegment.empty()

# Intro
lesson += spanish("Bienvenida a esta prueba del curso de griego koiné. Hoy aprenderás tu primer saludo en el idioma del Nuevo Testamento.")
lesson += pause(800)

# Opening dialogue
lesson += spanish("Escucha esta conversación entre dos personas en la Jerusalén del siglo primero.")
lesson += pause(600)
lesson += greek("Χαῖρε!", voice="el-GR-Chirp3-HD-Charon")  # male
lesson += pause(400)
lesson += greek("Εἰρήνη σοι.", voice="el-GR-Chirp3-HD-Kore")  # female
lesson += pause(400)
lesson += greek("Εἰρήνη σοι. Πόθεν εἶ;", voice="el-GR-Chirp3-HD-Charon")
lesson += pause(400)
lesson += greek("Ἐγώ εἰμι ἀπὸ Γαλιλαίας.", voice="el-GR-Chirp3-HD-Kore")
lesson += pause(1000)

# Breakdown
lesson += spanish("Escuchaste un saludo. El hombre dijo χαῖρε, que significa alégrate, o simplemente, hola.")
lesson += pause(500)
lesson += spanish("La mujer respondió εἰρήνη σοι, que significa paz a ti. Este es el saludo más importante del Nuevo Testamento.")
lesson += pause(800)

# Teach χαῖρε
lesson += spanish("Escucha y repite. Χαῖρε.")
lesson += pause(300)
lesson += greek("Χαῖρε")
lesson += pause(3000)  # student repeats
lesson += greek("Χαῖρε")
lesson += pause(800)

# Teach εἰρήνη σοι
lesson += spanish("Ahora escucha. Εἰρήνη.")
lesson += pause(300)
lesson += greek("Εἰρήνη")
lesson += pause(3000)
lesson += greek("Εἰρήνη")
lesson += pause(600)

lesson += spanish("Εἰρήνη significa paz. Ahora la frase completa. Εἰρήνη σοι. Paz a ti.")
lesson += pause(300)
lesson += greek("Εἰρήνη σοι")
lesson += pause(3500)
lesson += greek("Εἰρήνη σοι")
lesson += pause(800)

lesson += spanish("σοι significa a ti.")
lesson += pause(500)

# First recall
lesson += spanish("¿Cómo dirías hola en griego?")
lesson += pause(4000)
lesson += greek("Χαῖρε")
lesson += pause(600)

lesson += spanish("¿Cómo dirías paz a ti?")
lesson += pause(4000)
lesson += greek("Εἰρήνη σοι")
lesson += pause(800)

# Teach ἐγώ εἰμι
lesson += spanish("Ahora aprende a decir yo soy. Escucha.")
lesson += pause(300)
lesson += greek("ἐγώ εἰμι")
lesson += pause(3500)
lesson += spanish("ἐγώ significa yo. εἰμι significa soy. ἐγώ εἰμι, yo soy.")
lesson += pause(300)
lesson += greek("ἐγώ εἰμι")
lesson += pause(3500)
lesson += greek("ἐγώ εἰμι")
lesson += pause(800)

# Teach πόθεν εἶ
lesson += spanish("En la conversación, el hombre preguntó πόθεν εἶ, que significa ¿de dónde eres?")
lesson += pause(300)
lesson += greek("Πόθεν εἶ;", voice="el-GR-Chirp3-HD-Charon")
lesson += pause(3500)
lesson += spanish("πόθεν significa de dónde. εἶ significa eres. πόθεν εἶ, ¿de dónde eres?")
lesson += pause(300)
lesson += greek("Πόθεν εἶ;")
lesson += pause(3500)
lesson += greek("Πόθεν εἶ;")
lesson += pause(800)

# GIR recall cycle
lesson += spanish("¿Cómo dirías yo soy?")
lesson += pause(4000)
lesson += greek("ἐγώ εἰμι")
lesson += pause(600)

lesson += spanish("¿Cómo dirías paz a ti?")
lesson += pause(4000)
lesson += greek("Εἰρήνη σοι")
lesson += pause(600)

lesson += spanish("¿Cómo preguntarías de dónde eres?")
lesson += pause(4500)
lesson += greek("Πόθεν εἶ;")
lesson += pause(600)

lesson += spanish("¿Cómo dirías hola?")
lesson += pause(4000)
lesson += greek("Χαῖρε")
lesson += pause(800)

# Combine into mini dialogue
lesson += spanish("Ahora imagina que alguien te saluda en el camino a Jerusalén. Te dice:")
lesson += pause(400)
lesson += greek("Χαῖρε! Πόθεν εἶ;", voice="el-GR-Chirp3-HD-Charon")
lesson += pause(500)
lesson += spanish("Respóndele con paz a ti, yo soy de Galilea.")
lesson += pause(5000)
lesson += greek("Εἰρήνη σοι. ἐγώ εἰμι ἀπὸ Γαλιλαίας.", voice="el-GR-Chirp3-HD-Kore")
lesson += pause(1000)

# Biblical verse
lesson += spanish("Escucha este versículo del evangelio de Lucas, capítulo veinticuatro, versículo treinta y seis. Jesús se apareció a sus discípulos y les dijo:")
lesson += pause(500)
lesson += greek("Εἰρήνη ὑμῖν.", voice="el-GR-Chirp3-HD-Charon")
lesson += pause(500)
lesson += spanish("Paz a ustedes. ὑμῖν significa a ustedes. Ya conoces σοι, a ti. ὑμῖν es el plural, a ustedes.")
lesson += pause(800)

# Closing
lesson += spanish("Excelente. En esta prueba aprendiste cuatro expresiones fundamentales. Χαῖρε, hola. Εἰρήνη σοι, paz a ti. ἐγώ εἰμι, yo soy. Y πόθεν εἶ, de dónde eres. En la siguiente lección aprenderás a decir tu nombre y a preguntar quién es alguien.")
lesson += pause(500)

# Export
output = "decks/test_5min.mp3"
os.makedirs("decks", exist_ok=True)
lesson.export(output, format="mp3")
duration = len(lesson) / 1000
print(f"✓ Generated: {output} ({duration:.0f}s = {duration/60:.1f} min)")
