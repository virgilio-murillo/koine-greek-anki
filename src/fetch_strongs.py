"""Fetch Strong's etymological data for all 290 compounds + their components."""
import xml.etree.ElementTree as ET
import unicodedata, json, re

# Parse Strong's
tree = ET.parse("data/strongs_greek.xml")
entries = tree.getroot().find("entries")

def normalize(s):
    return unicodedata.normalize("NFC", s)

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# Build lookups
strongs_by_lemma = {}
strongs_by_num = {}
strongs_stripped = {}

for entry in entries.findall("entry"):
    greek_el = entry.find("greek")
    if greek_el is None:
        continue
    lemma = normalize(greek_el.get("unicode", ""))
    num = entry.get("strongs", "").lstrip("0")
    deriv_el = entry.find("strongs_derivation")
    def_el = entry.find("strongs_def")

    # Extract text, resolving strongsref elements to G-numbers
    def extract_text(el):
        if el is None:
            return ""
        parts = []
        if el.text:
            parts.append(el.text)
        for child in el:
            if child.tag == "strongsref":
                lang = child.get("language", "")
                snum = child.get("strongs", "").lstrip("0")
                parts.append(f"G{snum}" if lang == "GREEK" else f"H{snum}")
            elif child.tag == "greek":
                parts.append(child.get("unicode", ""))
            else:
                parts.append("".join(child.itertext()))
            if child.tail:
                parts.append(child.tail)
        return "".join(parts).strip()

    data = {
        "number": f"G{num}",
        "lemma": lemma,
        "derivation": extract_text(deriv_el),
        "definition": extract_text(def_el),
    }
    strongs_by_lemma[lemma] = data
    strongs_by_num[f"G{num}"] = data
    strongs_stripped[strip_accents(lemma).lower()] = data

def lookup(word):
    """Look up a word in Strong's, trying exact then fuzzy match."""
    w = normalize(word)
    if w in strongs_by_lemma:
        return strongs_by_lemma[w]
    sw = strip_accents(word).lower()
    if sw in strongs_stripped:
        return strongs_stripped[sw]
    return None

def resolve_refs(text):
    """Replace G-number references with actual Greek words."""
    def repl(m):
        ref = m.group(0)
        if ref in strongs_by_num:
            return f"{strongs_by_num[ref]['lemma']} ({ref})"
        return ref
    return re.sub(r'G\d+', repl, text)

# Load enriched cards
with open("data/matthew/compounds_enriched.json") as f:
    cards = json.load(f)

# Collect all words we need to look up
all_words = set()
for c in cards:
    all_words.add(c["lemma"])
    for comp in c["components"]:
        all_words.add(comp["greek"].strip("-"))

# Look up everything
found = 0
not_found = []
for word in sorted(all_words):
    result = lookup(word)
    if result:
        found += 1
    else:
        not_found.append(word)

print(f"Words to look up: {len(all_words)}")
print(f"Found in Strong's: {found}")
print(f"Not found: {len(not_found)}")
if not_found:
    print(f"Missing: {not_found[:20]}")

# Enrich cards
for card in cards:
    # Main word
    result = lookup(card["lemma"])
    if result:
        card["strongs_number"] = result["number"]
        card["strongs_derivation"] = resolve_refs(result["derivation"])
        card["strongs_definition"] = result["definition"]

    # Components
    for comp in card["components"]:
        word = comp["greek"].strip("-")
        result = lookup(word)
        if result:
            comp["strongs_number"] = result["number"]
            comp["strongs_derivation"] = resolve_refs(result["derivation"])
            comp["strongs_definition"] = result["definition"]

with open("data/matthew/compounds_enriched.json", "w") as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

# Show sample
for c in cards:
    if c["lemma"] == "ἐπιτρέπω":
        print(f"\n=== {c['lemma']} ===")
        print(f"Strong's: {c.get('strongs_number','')}")
        print(f"Derivation: {c.get('strongs_derivation','')}")
        for comp in c["components"]:
            print(f"  Component {comp['greek']}: {comp.get('strongs_derivation','N/A')}")
        break

print("\nDone!")
