"""Generate lessons. Usage: python -m src.generate [--all | --range 1 10 | --lesson 5]"""
import sys, time
from .data import ALL_LESSONS
from .engine import build

def generate(lessons_to_build=None):
    all_vocab = []
    start = time.time()
    targets = lessons_to_build or ALL_LESSONS
    target_nums = {d["num"] for d in targets}

    for data in ALL_LESSONS:
        if data["num"] in target_nums:
            prev = list(all_vocab) if all_vocab else None
            print(f"Generating lesson {data['num']}...")
            build(data, prev_vocab=prev)
        for v in data["vocab"]:
            all_vocab.append({"gr": v["gr"], "es": v["es"]})
        for p in data["phrases"]:
            all_vocab.append({"gr": p["gr"], "es": p["es"]})

    elapsed = time.time() - start
    print(f"\n✓ {len(target_nums)} lessons generated in {elapsed/60:.1f} minutes")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or "--all" in args:
        generate()
    elif "--range" in args:
        i = args.index("--range")
        lo, hi = int(args[i+1]), int(args[i+2])
        generate([d for d in ALL_LESSONS if lo <= d["num"] <= hi])
    elif "--lesson" in args:
        i = args.index("--lesson")
        n = int(args[i+1])
        generate([d for d in ALL_LESSONS if d["num"] == n])
