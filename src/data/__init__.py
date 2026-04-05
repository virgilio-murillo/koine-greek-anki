"""Lesson data index — loads all 90 lessons into a single ordered list."""
from .lesson_data_01_05 import L1, L2, L3, L4, L5
from .lesson_data_06_08 import L6, L7, L8
from .lesson_data_09_10 import L9, L10
from .lesson_data_11_15 import L11, L12, L13, L14, L15
from .lesson_data_16_20 import L16, L17, L18, L19, L20
from .lesson_data_21_25 import L21, L22, L23, L24, L25
from .lesson_data_26_30 import L26, L27, L28, L29, L30
from .lesson_data_31_35 import L31, L32, L33, L34, L35
from .lesson_data_36_40 import L36, L37, L38, L39, L40
from .lesson_data_41_45 import L41, L42, L43, L44, L45
from .lesson_data_46_50 import L46, L47, L48, L49, L50
from .lesson_data_51_55 import L51, L52, L53, L54, L55
from .lesson_data_56_60 import L56, L57, L58, L59, L60
from .lesson_data_61_65 import L61, L62, L63, L64, L65
from .lesson_data_66_70 import L66, L67, L68, L69, L70
from .lesson_data_71_75 import L71, L72, L73, L74, L75
from .lesson_data_76_80 import L76, L77, L78, L79, L80
from .lesson_data_81_85 import L81, L82, L83, L84, L85
from .lesson_data_86_90 import L86, L87, L88, L89, L90

ALL_LESSONS = [
    L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,
    L11,L12,L13,L14,L15,L16,L17,L18,L19,L20,
    L21,L22,L23,L24,L25,L26,L27,L28,L29,L30,
    L31,L32,L33,L34,L35,L36,L37,L38,L39,L40,
    L41,L42,L43,L44,L45,L46,L47,L48,L49,L50,
    L51,L52,L53,L54,L55,L56,L57,L58,L59,L60,
    L61,L62,L63,L64,L65,L66,L67,L68,L69,L70,
    L71,L72,L73,L74,L75,L76,L77,L78,L79,L80,
    L81,L82,L83,L84,L85,L86,L87,L88,L89,L90,
]

def get_lesson(n):
    """Get lesson by number (1-90)."""
    return ALL_LESSONS[n - 1]
