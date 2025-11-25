import random
import re
from collections import deque

from discord import ClientUser, Message
from rapidfuzz import fuzz

import util

RESPONSES = [
    "Yes",
    "Yeah",
    "Yep",
    "Mhm",
    "Yea",
    "Absolutely",
    "Indeed",
    "Without a doubt",
    "Obviously",
    "Indubitably",
]

KEY_PHRASES = [
    "is this true",
    "is this right",
    "is that true",
    "is that right",
    "is it true",
    "is it right",
    "are you sure",
    "is this correct",
    "is that correct",
    "is this real",
    "can you verify",
    "is that accurate",
]

PATTERNS = [
    r"\bis (this|that|it) (true|right)\b",
    r"\bare you sure\b",
    r"\b(true|right)\??$",
]

_last_replies: deque[str] = deque(maxlen=3)


FLEX_PATTERN = re.compile(r"is\s+(?:this|that|it)\s+\w*\s*(true|right)")
ALT_PATTERN = re.compile(r"(?:this|that|it)\s+is\s+(true|right)")


def contains_truth_question(text: str) -> bool:
    text = util.normalize(util.strip_discord_markup(text))

    # check direct patterns (strict)
    for p in PATTERNS:
        if re.search(p, text):
            return True

    # flexible phrasing
    if re.search(FLEX_PATTERN, text):
        return True

    # reversed phrasing
    if re.search(ALT_PATTERN, text):
        return True

    # fuzzy "contains" match
    for p in KEY_PHRASES:
        if fuzz.partial_ratio(text, p) >= 80:
            return True

    return False


def pick_truth_reply_simple() -> str:
    candidates: list[str] = [
        r for r in RESPONSES if r not in _last_replies
    ] or RESPONSES
    reply: str = random.choice(candidates)
    _last_replies.append(reply)
    return reply
