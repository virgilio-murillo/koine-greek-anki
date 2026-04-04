"""Generate all 10 lessons."""
import sys, os, time
sys.path.insert(0, ".")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/.config/gcloud/koine-tts-key.json")

from lesson_engine import build_lesson

start = time.time()

from lessons_01_02 import lesson_1, lesson_2
print("Generating lessons 1-2...")
build_lesson(lesson_1(), 1)
build_lesson(lesson_2(), 2)

from lessons_03_04 import lesson_3, lesson_4
print("Generating lessons 3-4...")
build_lesson(lesson_3(), 3)
build_lesson(lesson_4(), 4)

from lessons_05_06 import lesson_5, lesson_6
print("Generating lessons 5-6...")
build_lesson(lesson_5(), 5)
build_lesson(lesson_6(), 6)

from lessons_07_08 import lesson_7, lesson_8
print("Generating lessons 7-8...")
build_lesson(lesson_7(), 7)
build_lesson(lesson_8(), 8)

from lessons_09_10 import lesson_9, lesson_10
print("Generating lessons 9-10...")
build_lesson(lesson_9(), 9)
build_lesson(lesson_10(), 10)

elapsed = time.time() - start
print(f"\n✓ All 10 lessons generated in {elapsed/60:.1f} minutes")
