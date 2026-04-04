"""Download LXX Septuagint lemma data from openscriptures/GreekResources.
Downloads 60 books of lemmatized Greek text (~30MB) into data/lxx-lemmas/.
Usage: python src/download_lxx.py
"""
import json, urllib.request, os

OUT_DIR = "data/lxx-lemmas"
BASE_URL = "https://api.github.com/repos/openscriptures/GreekResources/contents/LxxLemmas"

os.makedirs(OUT_DIR, exist_ok=True)

req = urllib.request.Request(BASE_URL, headers={"User-Agent": "Mozilla/5.0"})
files = json.loads(urllib.request.urlopen(req).read())
js_files = [f for f in files if f['name'].endswith('.js')]

print(f"Downloading {len(js_files)} LXX books...")
for i, f in enumerate(js_files):
    out_path = os.path.join(OUT_DIR, f['name'])
    if os.path.exists(out_path):
        continue
    req = urllib.request.Request(f['download_url'], headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req).read()
    with open(out_path, 'wb') as fout:
        fout.write(data)
    if (i + 1) % 10 == 0:
        print(f"  {i+1}/{len(js_files)}...")

print(f"Done. {len(js_files)} books saved to {OUT_DIR}/")
