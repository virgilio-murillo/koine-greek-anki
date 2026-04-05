"""Pimsleur lesson builder — generates full audio lessons from structured data."""
import random
from pydub import AudioSegment
from .tts import es, gr, extra_phrases, M, F, P

def spd(n):
    return 0.75 if n <= 7 else (0.85 if n <= 15 else 1.0)

def build(data, prev_vocab=None, output_dir="decks/lessons"):
    """Generate full Pimsleur lesson from structured data."""
    import os
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
        # Deduplicate by greek text, sample from ALL prev (not just last 8)
        seen = set()
        unique = []
        for it in reversed(prev):
            if it["gr"] not in seen:
                seen.add(it["gr"])
                unique.append(it)
        random.seed(n); random.shuffle(unique)
        for it in unique[:6]:
            prompt = it["es"].rstrip("?.,;").split(",")[0]  # first meaning, clean punctuation
            L += es(f"¿Cómo dirías {prompt}?") + P(4000) + gr(it["gr"], speed=s) + P(500)
        L += P(300)

    # 3. NEW VOCABULARY — with interleaved GIR
    vocab = data["vocab"]
    for i, w in enumerate(vocab):
        vo = w.get("voice", F)
        L += es(w["note_es"]) + P(300)
        L += gr(w["gr"], voice=vo, speed=s) + P(3500)
        L += gr(w["gr"], voice=vo, speed=s) + P(800)
        for phrase in extra_phrases(w.get("note_es",""), w["gr"]):
            L += gr(phrase, voice=vo, speed=s) + P(3500)
        if len(w["gr"]) > 8:
            L += es("Escucha una vez más.") + P(300)
            L += gr(w["gr"], voice=vo, speed=s) + P(3500) + gr(w["gr"], voice=vo, speed=s) + P(800)
        if i > 0:
            pv = vocab[i-1]
            L += es(f"¿Cómo dirías {pv['es']}?") + P(4000) + gr(pv["gr"], speed=s) + P(500)
        if i > 2:
            pv2 = vocab[i-3]
            L += es(f"¿Cómo dirías {pv2['es']}?") + P(4000) + gr(pv2["gr"], speed=s) + P(500)

    # 4. PHRASE BUILDING + GIR
    phrases = data["phrases"]
    for i, ph in enumerate(phrases):
        L += es(ph["prompt_es"]) + P(300)
        L += gr(ph["gr"], speed=s) + P(4000)
        L += gr(ph["gr"], speed=s) + P(800)
        if i < len(vocab):
            v = vocab[i]
            L += es(f"¿Cómo dirías {v['es']}?") + P(4000) + gr(v["gr"], speed=s) + P(500)
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

    # 7. GIR CYCLE 3 — rapid fire
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
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"lesson_{n:02d}.mp3")
    L.export(path, format="mp3")
    dur = len(L)/1000
    print(f"  ✓ Lesson {n}: {path} ({dur:.0f}s = {dur/60:.1f} min)")
    return path
