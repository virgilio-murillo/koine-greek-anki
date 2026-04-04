"""Generate all 10 lessons using the Pimsleur engine."""
import sys, os, time
sys.path.insert(0, ".")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/.config/gcloud/koine-tts-key.json")

from pimsleur_engine import build
from lesson_data_01_05 import L1, L2, L3, L4, L5
from lesson_data_06_08 import L6, L7, L8
from lesson_data_09_10 import L9, L10

lessons = [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10]

# Build cumulative vocab for review
all_vocab = []
start = time.time()

for i, data in enumerate(lessons):
    prev = list(all_vocab) if all_vocab else None
    print(f"Generating lesson {data['num']}...")
    build(data, prev_vocab=prev)
    # Add this lesson's vocab to cumulative list
    for v in data["vocab"]:
        all_vocab.append({"gr": v["gr"], "es": v["es"]})
    for p in data["phrases"]:
        all_vocab.append({"gr": p["gr"], "es": p["es"]})

elapsed = time.time() - start
print(f"\n✓ All 10 lessons generated in {elapsed/60:.1f} minutes")
