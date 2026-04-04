# Lessons Learned — Koine Greek Course Development

What we learned building this course. For any AI agent continuing this project.

## 1. TTS for Ancient Greek

**Problem**: Google Cloud TTS only supports Modern Greek (el-GR). Koine Greek uses polytonic diacritics (breathing marks, circumflex, iota subscript) that Modern Greek TTS doesn't handle well.

**Solution**: 
- `to_mono()` function strips polytonic → monotonic before sending to TTS
- Byzantine/Modern pronunciation IS phonetically identical to Koine — the TTS output sounds correct
- **Chirp3-HD voices fail on short words** (1-2 syllables like σοι, οὐ, ναί) producing ~0.3s silent audio
- **Fix**: Wavenet-B as fallback — it handles short words correctly
- Implementation: check audio duration after TTS call; if < 400ms, retry with Wavenet-B

**Key code pattern**:
```python
audio = tts_chirp3(word)
if len(audio) < 400:  # TTS failure
    audio = tts_wavenet(word)  # fallback
```

## 2. Koine vs Modern Greek Contamination

**Critical rule**: The pronunciation is the same, but vocabulary and grammar are DIFFERENT.

**Vocabulary blacklist** (Modern words that don't exist in Koine):
- νερό (water) → use ὕδωρ
- σπίτι (house) → use οἶκος/οἰκία  
- ψωμί (bread) → use ἄρτος
- πόρτα (door) → use θύρα
- All Turkish/Italian loanwords (post-1453)

**False friends** (same word, different meaning):
- παρακαλέω: Koine = "beseech/exhort", NOT "please"
- ῥῆμα: Koine = "utterance/word spoken", NOT "verb"
- δουλεύω: Koine = "be a slave", NOT "work at a job"
- σημεῖον: Koine = "miraculous sign", NOT "point/mark"

**Grammar differences** (Koine has, Modern lost):
- Dative case (Modern uses σε + accusative)
- Infinitive (Modern uses να + subjunctive)
- Synthetic future (-σω suffix, Modern uses θα)
- Genitive absolute
- Fully declined participles

**Verification method**: Extract all Greek words from lessons, check each against MorphGNT (NT) + LXX lemma lists. If not attested in either, it's suspicious.

## 3. Pimsleur Method Implementation

**Core structure** (30 min lesson):
1. Opening dialogue (2 min) — student just listens
2. Review previous lessons (3 min) — GIR from earlier lessons
3. New vocabulary introduction (7 min) — 5-8 words, back-chaining
4. Phrase building + GIR cycle 1 (6 min) — combine words into phrases
5. GIR cycle 2 — all vocab shuffled (4 min)
6. Dialogue reconstruction (5 min) — student plays a role
7. Rapid fire GIR cycle 3 (2 min)
8. Biblical verse + closing (1 min)

**Graduated Interval Recall**: Within a lesson, a word appears at ~5s, 25s, 2min, 10min intervals. Across lessons, words from previous lessons are mixed into review sections.

**Our lessons average ~11 min** (not 30) because pauses are shorter than real Pimsleur. This is intentional — the user preferred shorter pauses.

## 4. Biblical Scenario Design

**What works**: Setting lessons in 1st century Palestine with real NT dialogue scenarios:
- Marketplace (Jn 6:5-9)
- Road encounters (Lc 24:13-17)
- Temple/synagogue (Lc 4:16)
- Healing scenes (Mc 10:51)
- Last Supper (Mt 26:26)

**Phrase verification**: Every Greek phrase taught must be attested in the NT or Septuagint. We caught one Modern Greek calque early: "Τί ἐστιν τὸ ὄνομά σου;" should be "Τί ὄνομά σοι;" (Mc 5:9).

## 5. Vocabulary Selection

**Data-driven**: We extracted the actual frequency list from MorphGNT:
- Top 310 words = 80% of NT text
- Top 600 words = 90% of NT text
- Teach by frequency, not by textbook chapter order

**Grammar introduction order** (for audio-first, NOT textbook):
1. εἰμί (to be) — lesson 1
2. Nominative/accusative — lessons 1-8
3. Present active -ω verbs — lessons 4-8
4. Genitive (possession) — lessons 12-13
5. Dative — lessons 1 (σοι), 13 (αὐτῷ)
6. Aorist (past) — lessons 25-26
7. Imperative — lessons 13, 27-28
8. Participios — lesson 42
9. Subjunctive — lesson 39, 44
10. Future — lesson 40

## 6. Production Pipeline

**Architecture**:
```
lesson_data_*.py (structured content: vocab, phrases, dialogue, verse)
    ↓
pimsleur_engine.py (auto-generates GIR cycles, phrase building, reconstruction)
    ↓
TTS APIs (Polly for Spanish, Google TTS for Greek)
    ↓
pydub assembly → MP3
```

**Caching**: All TTS calls are cached by content hash in /tmp/tts_cache/. Regenerating a lesson only re-generates changed segments.

**Cost**: ~$26 total for 90 lessons (covered by Google Cloud $300 free credit + free AWS Polly).

## 7. Quality Assurance

**Automated checks we ran**:
1. File integrity (ffprobe all 90 files)
2. Duration sanity (all 9.5-14.7 min)
3. Silent segment detection (found 26 TTS failures, fixed with Wavenet-B fallback)
4. Modern Greek contamination scan (0 blacklisted words found)
5. NT/LXX attestation check (all words verified)

**What we'd add for production**:
- AWS Transcribe for speech-to-text verification (two-pass: es-US + el-GR)
- A/B testing different voice combinations
- User feedback loop after each lesson
