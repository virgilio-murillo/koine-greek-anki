# Pimsleur Koine Greek Audio Course — Project Notes

## Status
- ✅ 5-minute test generated and approved (decks/test_5min.mp3)
- ⬜ 15-minute test (next step)
- ⬜ 10 full lessons (after 15-min test feedback)
- ⬜ Remaining 80 lessons

## Approved Format
- Lessons: 30 min each, Pimsleur method (anticipation + graduated interval recall)
- Greek speed: 75% for lessons 1-7, 85% for 8-15, 100% for 16+
- Narrator: female, Spanish, rotates every 10 lessons
- Greek voices: Google Cloud TTS Chirp3-HD (Kore=female, Charon=male)
- Spanish narrator: Amazon Polly (Mia, neural, es-MX) — free on user's AWS
- User loved the test — no changes to format, voices, pauses, or flow

## TTS Configuration
- Google Cloud credentials: ~/.config/gcloud/koine-tts-key.json
- Project: koine-greek-tts
- Service account: tts-generator@koine-greek-tts.iam.gserviceaccount.com
- $300 free credit available
- IMPORTANT: Koine Greek text must be converted to monotonic before sending to TTS (polytonic → monotonic, see to_monotonic() in generate_test_5min.py)

## Voice Assignments
| Role | Service | Voice | Language |
|---|---|---|---|
| Narrator (lessons 1-10) | Polly | Mia (neural) | es-MX |
| Narrator (lessons 11-20) | Polly | Mia (generative) or Google es-US female | es-MX/es-US |
| Narrator (lessons 21-30) | Google TTS | es-ES female | es-ES |
| Greek female speaker | Google TTS | el-GR-Chirp3-HD-Kore | el-GR |
| Greek male speaker | Google TTS | el-GR-Chirp3-HD-Charon | el-GR |

## Curriculum (90 lessons, 3 levels)
- Level 1 (1-30): "Ὁ Ξένος" — survival Greek, ~200 words
- Level 2 (31-60): "Ὁ Μαθητής" — past tense, parables, ~400 cumulative
- Level 3 (61-90): "Ὁ Κήρυξ" — reading texts, epistles, ~600 cumulative
- 600 words = ~90% of NT text coverage

## Key Technical Notes
- pydub for audio assembly (requires ffmpeg)
- TTS cache at /tmp/tts_cache/ to avoid re-generating segments
- Back-chaining for long words (teach from end backward)
- GIR intervals: 5s → 25s → 2min → 10min → across lessons
- 5-8 new root vocabulary per lesson, 15-20 phrases/forms

## Investigation Report
- Full Pimsleur research: investigation/31d52ff9/final_report.md (591 lines)
- Hermeneumata Pseudodositheana: authentic 1st-4th century conversation manuals for scenarios
- No Pimsleur course exists for any ancient language — this is a market gap

## Dependencies
```
pip install genanki py-sblgnt google-cloud-texttospeech boto3 pydub
brew install ffmpeg
```
