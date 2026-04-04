# Lessons Learned — Replicating for Other Languages

How to build a Pimsleur-style audio course for any ancient/biblical language using this same pipeline. Written for AI agents.

## Step-by-Step Replication Guide

### 1. Corpus & Frequency Analysis

**What you need**: A digitized, lemmatized text corpus of the target language.

| Language | Corpus Source | Lemmatized? |
|---|---|---|
| Koine Greek NT | MorphGNT (py-sblgnt) | ✅ Yes |
| Koine Greek LXX | openscriptures/LxxLemmas | ✅ Yes |
| Biblical Hebrew | ETCBC/bhsa (SHEBANQ) | ✅ Yes |
| Classical Latin | Perseus Digital Library | ✅ Yes |
| Aramaic | CAL (Comprehensive Aramaic Lexicon) | Partial |

**Extract**: Top 600 words by frequency. This covers ~90% of most biblical texts.

### 2. TTS Voice Selection

**The key question**: Is there a modern descendant language with TTS support?

| Ancient Language | Modern TTS Proxy | Works? |
|---|---|---|
| Koine Greek | Modern Greek (el-GR) | ✅ Byzantine pronunciation = Modern |
| Biblical Hebrew | Modern Hebrew (he-IL) | ⚠️ Vowels differ significantly |
| Classical Latin | Italian (it-IT) | ❌ Too different |
| Classical Arabic | Modern Standard Arabic (ar-SA) | ✅ Close enough |

**For Hebrew**: Modern Hebrew TTS (Google/Azure/AWS all support he-IL) can work but:
- Vowel pronunciation differs (Tiberian vs Modern Israeli)
- Stress patterns differ
- Some consonants merged (ע, ח, כ/ק)
- Consider using a custom voice model trained on liturgical Hebrew

**Fallback strategy**: For languages without TTS, use ElevenLabs voice cloning with a scholar's recording as the base voice.

### 3. Contamination Prevention

**CRITICAL**: The #1 risk is contaminating ancient language content with modern forms.

**Build these artifacts before writing any content**:

1. **Vocabulary blacklist**: Modern words absent from the ancient corpus
2. **False friends list**: Words that exist in both but mean different things
3. **Grammar difference checklist**: Features the ancient language has that the modern lost (or vice versa)
4. **Verification script**: Check every word against the corpus lemma list

**For Biblical Hebrew specifically**:
- Modern Hebrew has no construct state emphasis (סמיכות still exists but usage differs)
- Waw-consecutive (ויאמר) doesn't exist in Modern Hebrew
- Verbal system is completely different (Modern has no Qal perfect/imperfect distinction in the same way)
- Modern vocabulary: טלפון, מחשב, אוטובוס — obviously absent from Bible

### 4. Pimsleur Engine Architecture

The engine is language-agnostic. To adapt for a new language:

```python
# pimsleur_engine.py — change these:
NARRATOR_SERVICE = "polly"       # or google, azure
NARRATOR_VOICE = "Mia"           # Spanish narrator
NARRATOR_LANG = "es-MX"          # narrator language
TARGET_SERVICE = "google"         # TTS for target language
TARGET_VOICE = "he-IL-Wavenet-A" # Hebrew example
TARGET_LANG = "he-IL"            # target language code
FALLBACK_VOICE = "he-IL-Standard-A"  # for short words
```

**The lesson data format is universal**:
```python
lesson = {
    "num": 1,
    "intro_es": "...",           # narrator intro (any language)
    "dialogue": [(voice, text)], # target language dialogue
    "vocab": [{"gr": "שָׁלוֹם", "es": "paz", "note_es": "..."}],
    "phrases": [...],
    "recon": [...],              # dialogue reconstruction
    "verse": {...},              # scripture verse
    "closing_es": "...",
}
```

### 5. Curriculum Design Pattern

**Universal for any biblical language**:

| Phase | Lessons | Content |
|---|---|---|
| Survival | 1-10 | Greetings, names, origin, numbers, food, directions |
| Daily life | 11-20 | Family, time, body, adjectives, occupations |
| Faith basics | 21-30 | Past tense, commands, prayer, God/Lord, review |
| Narratives | 31-45 | Extended past, parables, healings, emotions |
| Theology | 46-60 | Epistolary style, community, suffering, key texts |
| Advanced reading | 61-75 | Passion narrative, argumentation, metaphors |
| Mastery | 76-90 | Continuous reading of famous passages, evaluation |

**For Hebrew**: Replace NT scenarios with Torah/Tanakh:
- Marketplace → Genesis narratives
- Temple → Tabernacle/Temple descriptions
- Parables → Proverbs/Wisdom literature
- Epistles → Psalms
- Passion → Exodus/Passover

### 6. Cost Estimation

For 90 lessons (~17 hours of audio):

| Component | Koine Greek Cost | Hebrew Estimate |
|---|---|---|
| Target language TTS | ~$16 (Google) | ~$16 (Google/Azure) |
| Narrator TTS | $0 (AWS Polly free tier) | $0 |
| Total | **~$16** | **~$16** |

Google Cloud gives $300 free credit to new accounts. AWS Polly is free for the first year (5M chars/month).

### 7. Quality Assurance Checklist

Before releasing any lesson:

- [ ] Every word verified against corpus (not modern)
- [ ] No modern grammar patterns (check language-specific list)
- [ ] No false friends used with wrong meaning
- [ ] All TTS segments > 400ms (no silent failures)
- [ ] File integrity check (ffprobe)
- [ ] Duration within expected range
- [ ] Biblical references verified

### 8. Hebrew-Specific Notes

If building a Biblical Hebrew course next:

**TTS**: Google Cloud TTS has `he-IL` with Wavenet voices. Modern Israeli pronunciation is acceptable for beginners (most Hebrew courses use it). Tiberian pronunciation would require custom voice.

**Corpus**: Use ETCBC/BHSA (Biblia Hebraica Stuttgartensia Amstelodamensis) — fully lemmatized, morphologically tagged, freely available.

**Script**: Hebrew TTS handles niqqud (vowel points) well. Send pointed text (בְּרֵאשִׁית) not unpointed (בראשית) for correct pronunciation.

**Frequency**: Top 600 Hebrew words cover ~80% of the Hebrew Bible (similar ratio to Greek NT).

**Key difference from Greek**: Hebrew has a much smaller vocabulary in the Bible (~8,000 unique words vs Greek NT's ~5,400) but the Hebrew Bible is much longer, so frequency distribution is different.
