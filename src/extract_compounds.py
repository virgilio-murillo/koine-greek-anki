"""Extract compound word candidates from any NT book (MorphGNT/SBLGNT).
Usage: python extract_compounds.py --book 1 --output data/matthew/compounds_raw.json
Book numbers: 1=Matthew, 2=Mark, 3=Luke, 4=John, ..., 27=Revelation
"""
import json, argparse, os
from pysblgnt import morphgnt_rows

BOOK_NAMES = {
    1:'matthew',2:'mark',3:'luke',4:'john',5:'acts',6:'romans',
    7:'1corinthians',8:'2corinthians',9:'galatians',10:'ephesians',
    11:'philippians',12:'colossians',13:'1thessalonians',14:'2thessalonians',
    15:'1timothy',16:'2timothy',17:'titus',18:'philemon',19:'hebrews',
    20:'james',21:'1peter',22:'2peter',23:'1john',24:'2john',25:'3john',
    26:'jude',27:'revelation'
}

PREFIXES = [
    'ἀπο', 'ἐπι', 'κατα', 'παρα', 'συν', 'ἀντι', 'ὑπο', 'ὑπερ',
    'προσ', 'εἰσ', 'ἐκ', 'μετα', 'περι', 'δια', 'ἀνα', 'πρό',
    'ἐν', 'εὐ', 'φιλ', 'ψευδ', 'πολυ', 'μισ', 'ὀλιγ', 'μονο', 'ὁμο', 'ἀ', 'δυσ'
]

def is_compound_candidate(lemma):
    if len(lemma) < 5:
        return False
    for p in PREFIXES:
        if lemma.startswith(p) and len(lemma) > len(p) + 2:
            return True
    return False

def extract(book_num, registry_path=None):
    """Extract compounds, optionally filtering against existing registry."""
    registry = set()
    if registry_path and os.path.exists(registry_path):
        with open(registry_path) as f:
            registry = set(json.load(f).keys())

    lemma_first_ref = {}
    lemma_pos = {}
    for row in morphgnt_rows(book_num):
        lemma = row['lemma']
        if lemma not in lemma_first_ref:
            bcv = row['bcv']
            ch, vs = int(bcv[2:4]), int(bcv[4:6])
            book_abbrev = BOOK_NAMES.get(book_num, str(book_num))[:2].capitalize()
            lemma_first_ref[lemma] = f"{book_abbrev} {ch}:{vs}"
            lemma_pos[lemma] = row['ccat-pos']

    compounds = sorted([
        {"lemma": l, "pos": lemma_pos[l], "first_ref": lemma_first_ref[l]}
        for l in lemma_first_ref
        if is_compound_candidate(l) and l not in registry
    ], key=lambda x: x['lemma'])

    return compounds, len(lemma_first_ref)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--book", type=int, required=True, help="Book number (1-27)")
    p.add_argument("--output", required=True, help="Output JSON path")
    p.add_argument("--registry", default="data/compounds_registry.json", help="Registry for dedup")
    args = p.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    compounds, total = extract(args.book, args.registry)
    with open(args.output, "w") as f:
        json.dump(compounds, f, ensure_ascii=False, indent=2)
    name = BOOK_NAMES.get(args.book, str(args.book))
    print(f"{name}: {total} lemmas, {len(compounds)} compound candidates (after dedup)")
