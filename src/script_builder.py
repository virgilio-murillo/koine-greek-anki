"""Lesson script generator — produces structured JSON for audio generation."""
import random, json, sys, os
sys.path.insert(0, ".")
from src.tts import M, F, extra_phrases

def spd(n):
    return 0.75 if n <= 7 else (0.85 if n <= 15 else 1.0)

def build_script(data, prev_vocab=None):
    """Generate lesson as structured JSON segments."""
    n = data["num"]; s = spd(n); prev = prev_vocab or []
    segs = []

    def es(text): segs.append({"lang": "es", "text": text})
    def gr(text, voice=F): segs.append({"lang": "gr", "text": text, "voice": voice, "speed": s})
    def pause(ms): segs.append({"lang": "silence", "ms": ms})

    # 1. INTRO + DIALOGUE
    es(data["intro_es"]); pause(800)
    for v, t in data["dialogue"]:
        gr(t, voice=v); pause(400)
    pause(600); es(data["context_es"]); pause(800)

    # 2. REVIEW PREVIOUS
    if prev:
        es("Antes de aprender palabras nuevas, repasemos."); pause(500)
        seen = set(); unique = []
        for it in reversed(prev):
            if it["gr"] not in seen: seen.add(it["gr"]); unique.append(it)
        random.seed(n); random.shuffle(unique)
        for it in unique[:6]:
            prompt = it["es"].rstrip("?.,;").split(",")[0]
            es(f"¿Cómo dirías {prompt}?"); pause(4000)
            gr(it["gr"]); pause(500)
        pause(300)

    # 3. VOCABULARY
    vocab = data["vocab"]
    for i, w in enumerate(vocab):
        vo = w.get("voice", F)
        es(w["note_es"]); pause(300)
        gr(w["gr"], voice=vo); pause(3500)
        gr(w["gr"], voice=vo); pause(800)
        for phrase in extra_phrases(w.get("note_es", ""), w["gr"]):
            gr(phrase, voice=vo); pause(3500)
        if len(w["gr"]) > 8:
            es("Escucha una vez más."); pause(300)
            gr(w["gr"], voice=vo); pause(3500)
            gr(w["gr"], voice=vo); pause(800)
        if i > 0:
            pv = vocab[i-1]
            es(f"¿Cómo dirías {pv['es']}?"); pause(4000)
            gr(pv["gr"]); pause(500)
        if i > 2:
            pv2 = vocab[i-3]
            es(f"¿Cómo dirías {pv2['es']}?"); pause(4000)
            gr(pv2["gr"]); pause(500)

    # 4. PHRASES
    phrases = data["phrases"]
    for i, ph in enumerate(phrases):
        es(ph["prompt_es"]); pause(300)
        gr(ph["gr"]); pause(4000)
        gr(ph["gr"]); pause(800)
        if i < len(vocab):
            v = vocab[i]
            es(f"¿Cómo dirías {v['es']}?"); pause(4000)
            gr(v["gr"]); pause(500)
        if i > 1:
            op = phrases[i-2]
            es(f"¿Cómo dirías {op['es']}?"); pause(4500)
            gr(op["gr"]); pause(500)

    # 5. GIR CYCLE 2
    es("Practiquemos todo junto."); pause(500)
    all_it = [(v["es"], v["gr"]) for v in vocab] + [(p["es"], p["gr"]) for p in phrases]
    if prev: all_it += [(pv["es"], pv["gr"]) for pv in prev[-4:]]
    random.shuffle(all_it)
    for e, g in all_it:
        es(f"¿Cómo dirías {e}?"); pause(4500)
        gr(g); pause(500)
    pause(300)

    # 6. RECON
    recon = data.get("recon", [])
    if recon:
        es("Ahora reconstruyamos la conversación. Tú participas."); pause(800)
        for r in recon:
            if r.get("other_gr"):
                gr(r["other_gr"], voice=r.get("other_voice", M)); pause(500)
            es(r["prompt_es"]); pause(5000)
            gr(r["answer_gr"], voice=r.get("answer_voice", F)); pause(600)

    # 7. RAPID FIRE
    es("Repaso rápido."); pause(400)
    final = [(v["es"], v["gr"]) for v in vocab] + [(p["es"], p["gr"]) for p in phrases[:5]]
    for e, g in final:
        es(e + "."); pause(3500)
        gr(g); pause(400)

    # 8. VERSE + CLOSING
    v = data.get("verse", {})
    if v:
        pause(300); es(v["ref_es"]); pause(500)
        gr(v["gr"], voice=v.get("voice", M)); pause(600)
        es(v["explain_es"]); pause(800)
    es(data["closing_es"]); pause(500)

    return {"lesson": n, "segments": segs}

if __name__ == "__main__":
    from src.data import ALL_LESSONS
    targets = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [1]
    all_vocab = []
    for data in ALL_LESSONS:
        if data["num"] in targets:
            prev = list(all_vocab) if all_vocab else None
            script = build_script(data, prev_vocab=prev)
            path = f"kiro-test/lesson_{data['num']:02d}_script.json"
            with open(path, "w") as f:
                json.dump(script, f, ensure_ascii=False, indent=2)
            n_es = sum(1 for s in script["segments"] if s["lang"] == "es")
            n_gr = sum(1 for s in script["segments"] if s["lang"] == "gr")
            print(f"L{data['num']}: {n_es} ES + {n_gr} GR segments → {path}")
        for v in data["vocab"]:
            all_vocab.append({"gr": v["gr"], "es": v["es"]})
        for p in data["phrases"]:
            all_vocab.append({"gr": p["gr"], "es": p["es"]})
