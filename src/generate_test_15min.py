"""Generate a 15-minute Pimsleur-style test lesson for Koine Greek.
Builds on the 5-min test: adds more vocabulary, longer GIR cycles, dialogue reconstruction.
"""
import boto3, os, unicodedata
from google.cloud import texttospeech
from pydub import AudioSegment

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/.config/gcloud/koine-tts-key.json")

polly = boto3.client("polly", region_name="us-east-1")
gtts = texttospeech.TextToSpeechClient()

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

def es(text, voice="Mia", engine="neural"):
    key = f"es_{voice}_{engine}_{hash(text)}.mp3"
    path = os.path.join(CACHE_DIR, key)
    if not os.path.exists(path):
        resp = polly.synthesize_speech(Text=text, OutputFormat="mp3", VoiceId=voice, Engine=engine, LanguageCode="es-MX")
        with open(path, "wb") as f:
            f.write(resp["AudioStream"].read())
    return AudioSegment.from_mp3(path)

def gr(text, voice="el-GR-Chirp3-HD-Kore", speed=0.75):
    mono = to_monotonic(text)
    key = f"gr_{voice}_{speed}_{hash(mono)}.mp3"
    path = os.path.join(CACHE_DIR, key)
    if not os.path.exists(path):
        resp = gtts.synthesize_speech(
            input=texttospeech.SynthesisInput(text=mono),
            voice=texttospeech.VoiceSelectionParams(language_code="el-GR", name=voice),
            audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3, speaking_rate=speed)
        )
        with open(path, "wb") as f:
            f.write(resp.audio_content)
    return AudioSegment.from_mp3(path)

M = "el-GR-Chirp3-HD-Charon"  # male Greek voice
F = "el-GR-Chirp3-HD-Kore"    # female Greek voice
P = AudioSegment.silent  # pause shortcut

print("Generating 15-minute lesson...")
L = AudioSegment.empty()

# ============================================================
# SECTION 1: INTRO + OPENING DIALOGUE (0:00 - 2:00)
# ============================================================
L += es("Bienvenida a la lección uno de griego koiné. Imagina que estás caminando por un camino polvoriento hacia Jerusalén. Es el siglo primero. Te encuentras con un hombre y una mujer que conversan. Escucha.")
L += P(800)

# Full dialogue (student just listens)
L += gr("Χαῖρε!", voice=M)
L += P(300)
L += gr("Εἰρήνη σοι.", voice=F)
L += P(300)
L += gr("Πόθεν εἶ;", voice=M)
L += P(300)
L += gr("Ἐγώ εἰμι ἀπὸ Γαλιλαίας. Καὶ σύ;", voice=F)
L += P(300)
L += gr("Ἐγώ εἰμι ἀπὸ Ἰερουσαλήμ.", voice=M)
L += P(300)
L += gr("Τί ἐστιν τὸ ὄνομά σου;", voice=F)
L += P(300)
L += gr("Τὸ ὄνομά μου Σίμων. Καὶ τὸ ὄνομά σου;", voice=M)
L += P(300)
L += gr("Μαρία.", voice=F)
L += P(1000)

L += es("No te preocupes si no entendiste todo. Al final de esta lección, podrás tener esta misma conversación.")
L += P(800)

# ============================================================
# SECTION 2: VOCABULARY — GREETINGS (2:00 - 5:00)
# ============================================================
L += es("Empecemos. El hombre dijo χαῖρε. Significa alégrate, o simplemente, hola. Escucha y repite.")
L += P(300)
L += gr("Χαῖρε", voice=M)
L += P(3500)
L += gr("Χαῖρε")
L += P(800)

L += es("La mujer respondió εἰρήνη σοι. Significa paz a ti. Es el saludo más importante del Nuevo Testamento. Escucha.")
L += P(300)
L += gr("Εἰρήνη σοι", voice=F)
L += P(3500)
L += es("Repite solo la primera palabra. Εἰρήνη. Paz.")
L += P(300)
L += gr("Εἰρήνη")
L += P(3500)
L += gr("Εἰρήνη")
L += P(600)

L += es("Ahora la frase completa. Εἰρήνη σοι. Paz a ti. σοι significa a ti.")
L += P(300)
L += gr("Εἰρήνη σοι")
L += P(3500)
L += gr("Εἰρήνη σοι")
L += P(800)

# First GIR recall
L += es("¿Cómo dirías hola en griego?")
L += P(4000)
L += gr("Χαῖρε")
L += P(600)

L += es("¿Cómo dirías paz a ti?")
L += P(4000)
L += gr("Εἰρήνη σοι")
L += P(800)

# ============================================================
# SECTION 3: VOCABULARY — IDENTITY (5:00 - 8:30)
# ============================================================
L += es("Ahora aprende a decir yo soy. Escucha.")
L += P(300)
L += gr("ἐγώ εἰμι")
L += P(3500)
L += es("ἐγώ significa yo. εἰμι significa soy. Repite. ἐγώ εἰμι.")
L += P(300)
L += gr("ἐγώ εἰμι")
L += P(3500)
L += gr("ἐγώ εἰμι")
L += P(800)

L += es("El hombre preguntó πόθεν εἶ. Significa ¿de dónde eres? Escucha.")
L += P(300)
L += gr("Πόθεν εἶ;", voice=M)
L += P(3500)
L += es("πόθεν significa de dónde. εἶ significa eres. Repite la pregunta.")
L += P(300)
L += gr("Πόθεν εἶ;")
L += P(4000)
L += gr("Πόθεν εἶ;")
L += P(800)

# GIR cycle
L += es("¿Cómo dirías yo soy?")
L += P(4000)
L += gr("ἐγώ εἰμι")
L += P(500)

L += es("¿Cómo preguntarías de dónde eres?")
L += P(4500)
L += gr("Πόθεν εἶ;")
L += P(500)

L += es("¿Cómo dirías paz a ti?")
L += P(4000)
L += gr("Εἰρήνη σοι")
L += P(800)

# Teach "from Jerusalem / from Galilee"
L += es("La mujer dijo ἀπὸ Γαλιλαίας. Significa de Galilea. ἀπό significa de o desde. Escucha.")
L += P(300)
L += gr("ἀπὸ Γαλιλαίας")
L += P(3500)
L += gr("ἀπὸ Γαλιλαίας")
L += P(600)

L += es("El hombre dijo ἀπὸ Ἰερουσαλήμ. De Jerusalén.")
L += P(300)
L += gr("ἀπὸ Ἰερουσαλήμ", voice=M)
L += P(3500)
L += gr("ἀπὸ Ἰερουσαλήμ")
L += P(600)

L += es("Ahora di la frase completa. Yo soy de Jerusalén.")
L += P(5000)
L += gr("ἐγώ εἰμι ἀπὸ Ἰερουσαλήμ")
L += P(800)

# ============================================================
# SECTION 4: VOCABULARY — NAME (8:30 - 11:00)
# ============================================================
L += es("La mujer preguntó τί ἐστιν τὸ ὄνομά σου. Significa ¿cuál es tu nombre? Escucha.")
L += P(300)
L += gr("Τί ἐστιν τὸ ὄνομά σου;", voice=F)
L += P(4000)
L += es("Vamos parte por parte. τί significa qué o cuál.")
L += P(300)
L += gr("τί")
L += P(2500)
L += es("ἐστιν significa es.")
L += P(300)
L += gr("ἐστιν")
L += P(2500)
L += es("τὸ ὄνομα significa el nombre.")
L += P(300)
L += gr("τὸ ὄνομα")
L += P(3000)
L += es("σου significa tu o de ti.")
L += P(300)
L += gr("σου")
L += P(2500)
L += es("Ahora la pregunta completa. ¿Cuál es tu nombre?")
L += P(300)
L += gr("Τί ἐστιν τὸ ὄνομά σου;")
L += P(4500)
L += gr("Τί ἐστιν τὸ ὄνομά σου;")
L += P(800)

L += es("El hombre respondió τὸ ὄνομά μου Σίμων. Mi nombre es Simón. μου significa mi o de mí.")
L += P(300)
L += gr("Τὸ ὄνομά μου Σίμων.", voice=M)
L += P(4000)
L += gr("Τὸ ὄνομά μου Σίμων.")
L += P(800)

# GIR cycle — all words so far
L += es("¿Cómo preguntarías cuál es tu nombre?")
L += P(5000)
L += gr("Τί ἐστιν τὸ ὄνομά σου;")
L += P(500)

L += es("¿Cómo dirías hola?")
L += P(3500)
L += gr("Χαῖρε")
L += P(500)

L += es("¿Cómo dirías mi nombre es María?")
L += P(5000)
L += gr("Τὸ ὄνομά μου Μαρία.")
L += P(500)

L += es("¿Cómo dirías yo soy de Galilea?")
L += P(5000)
L += gr("ἐγώ εἰμι ἀπὸ Γαλιλαίας")
L += P(500)

L += es("¿Cómo dirías paz a ti?")
L += P(4000)
L += gr("Εἰρήνη σοι")
L += P(500)

L += es("¿Cómo preguntarías de dónde eres?")
L += P(4500)
L += gr("Πόθεν εἶ;")
L += P(800)

# ============================================================
# SECTION 5: TEACH "AND YOU?" + DIALOGUE RECONSTRUCTION (11:00 - 13:30)
# ============================================================
L += es("La mujer dijo καὶ σύ, que significa y tú. καί significa y. σύ significa tú.")
L += P(300)
L += gr("καὶ σύ")
L += P(3000)
L += gr("καὶ σύ")
L += P(800)

L += es("Ahora vamos a reconstruir la conversación completa. Tú serás Simón. María te saluda. Respóndele.")
L += P(800)

L += gr("Χαῖρε!", voice=F)
L += P(500)
L += es("Dile paz a ti.")
L += P(4000)
L += gr("Εἰρήνη σοι.", voice=M)
L += P(500)

L += gr("Πόθεν εἶ;", voice=F)
L += P(500)
L += es("Dile que eres de Jerusalén.")
L += P(5000)
L += gr("ἐγώ εἰμι ἀπὸ Ἰερουσαλήμ.", voice=M)
L += P(500)

L += es("Pregúntale de dónde es ella.")
L += P(5000)
L += gr("Πόθεν εἶ;", voice=M)
L += P(400)
L += gr("ἐγώ εἰμι ἀπὸ Γαλιλαίας.", voice=F)
L += P(500)

L += es("Pregúntale su nombre.")
L += P(5000)
L += gr("Τί ἐστιν τὸ ὄνομά σου;", voice=M)
L += P(400)
L += gr("Τὸ ὄνομά μου Μαρία. Καὶ τὸ ὄνομά σου;", voice=F)
L += P(500)

L += es("Dile tu nombre. Mi nombre es Simón.")
L += P(5000)
L += gr("Τὸ ὄνομά μου Σίμων.", voice=M)
L += P(1000)

# ============================================================
# SECTION 6: FINAL GIR + BIBLICAL VERSE + CLOSING (13:30 - 15:00)
# ============================================================
L += es("Muy bien. Repasemos rápido.")
L += P(400)

L += es("Hola.")
L += P(3500)
L += gr("Χαῖρε")
L += P(400)

L += es("Paz a ti.")
L += P(3500)
L += gr("Εἰρήνη σοι")
L += P(400)

L += es("Yo soy.")
L += P(3500)
L += gr("ἐγώ εἰμι")
L += P(400)

L += es("¿De dónde eres?")
L += P(4000)
L += gr("Πόθεν εἶ;")
L += P(400)

L += es("¿Cuál es tu nombre?")
L += P(4500)
L += gr("Τί ἐστιν τὸ ὄνομά σου;")
L += P(400)

L += es("De Jerusalén.")
L += P(4000)
L += gr("ἀπὸ Ἰερουσαλήμ")
L += P(400)

L += es("Y tú.")
L += P(3000)
L += gr("καὶ σύ")
L += P(800)

# Biblical verse
L += es("Escucha este versículo del evangelio de Juan, capítulo uno, versículo diecinueve. Los sacerdotes de Jerusalén enviaron mensajeros a Juan el Bautista y le preguntaron:")
L += P(500)
L += gr("Σὺ τίς εἶ;", voice=M)
L += P(600)
L += es("Tú, ¿quién eres? Reconoces las palabras. σύ es tú. τίς es quién. εἶ es eres.")
L += P(500)
L += gr("Σὺ τίς εἶ;")
L += P(600)
L += es("Y Juan respondió:")
L += P(400)
L += gr("ἐγώ εἰμι φωνὴ βοῶντος ἐν τῇ ἐρήμῳ.", voice=M)
L += P(500)
L += es("Yo soy voz del que clama en el desierto. Ya conoces ἐγώ εἰμι, yo soy. Pronto aprenderás el resto.")
L += P(800)

# Closing
L += es("Excelente. En esta lección aprendiste a saludar, a decir de dónde eres, y a preguntar el nombre de alguien. Aprendiste ocho expresiones en griego koiné. En la siguiente lección aprenderás a decir sí, no, y a preguntar si alguien habla griego. Εἰρήνη σοι.")
L += P(500)

# Export
output = "decks/test_15min.mp3"
os.makedirs("decks", exist_ok=True)
L.export(output, format="mp3")
duration = len(L) / 1000
print(f"✓ Generated: {output} ({duration:.0f}s = {duration/60:.1f} min)")
