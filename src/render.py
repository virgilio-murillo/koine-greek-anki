"""Generate MP3 from structured lesson JSON."""
import json, re, sys, os
sys.path.insert(0, ".")
from pydub import AudioSegment
from src.tts import es, gr, M, F, P

_GREEK = re.compile(r'([\u0370-\u03FF\u1F00-\u1FFF][\u0370-\u03FF\u1F00-\u1FFF\u0300-\u036F\s\u0027\u1FBD]*[\u0370-\u03FF\u1F00-\u1FFF\u0300-\u036F]|[\u0370-\u03FF\u1F00-\u1FFF])')

def render_es(text, speed=0.75):
    """Render Spanish text, switching to Greek TTS for any Greek words."""
    parts = _GREEK.split(text)
    audio = AudioSegment.empty()
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if _GREEK.match(part):
            audio += gr(part, speed=speed)
        else:
            audio += es(part)
    return audio

def render(script_path, output_dir="decks/lessons"):
    with open(script_path) as f:
        script = json.load(f)
    n = script['lesson']
    audio = AudioSegment.empty()
    for seg in script['segments']:
        if seg['lang'] == 'es':
            speed = seg.get('speed', 0.75)
            audio += render_es(seg['text'], speed)
        elif seg['lang'] == 'gr':
            voice = seg.get('voice', F)
            speed = seg.get('speed', 0.75)
            audio += gr(seg['text'], voice=voice, speed=speed)
        elif seg['lang'] == 'silence':
            audio += P(seg['ms'])
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"lesson_{n:02d}.mp3")
    audio.export(path, format="mp3")
    dur = len(audio) / 1000
    print(f"  ✓ Lesson {n}: {path} ({dur:.0f}s = {dur/60:.1f} min)")
    return path

if __name__ == '__main__':
    for p in sys.argv[1:]:
        render(p)
