import random
import re
import string
from collections import deque

from discord import ClientUser, Message
from rapidfuzz import fuzz

_DISCORD_MARKUP = re.compile(
    (
        r"<(?:[@#&!]\d+|a?:\w+:\d+)>|"  # mentions, custom emoji
        r"[\U0001f600-\U0001f64f"  # emoticons
        r"\U0001f300-\U0001f5ff"  # symbols & pictographs
        r"\U0001f680-\U0001f6ff"  # transport & map
        r"\U0001f1e0-\U0001f1ff]"  # flags
    ),
    flags=re.UNICODE,
)
_PUNCT = string.punctuation.replace("?", "")

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
    "is that true",
    "is it true",
    "are you sure",
    "is this correct",
    "is that correct",
    "is this real",
    "can you verify",
    "is that accurate",
]

PATTERNS = [
    r"\bis (this|that|it) true\b",
    r"\bare you sure\b",
    r"\btrue\??$",
]

_last_replies: deque[str] = deque(maxlen=3)


def strip_discord_markup(text: str) -> str:
    return _DISCORD_MARKUP.sub(" ", text)


def normalize(text: str) -> str:
    text = text.lower()
    # remove punctuation besides ? marks
    for p in _PUNCT:
        text = text.replace(p, " ")
    return " ".join(text.split())


FLEX_PATTERN = re.compile(r"is\s+(?:this|that|it)\s+\w*\s*true")
ALT_PATTERN = re.compile(r"(?:this|that|it)\s+is\s+true")


def contains_truth_question(text: str) -> bool:
    text = normalize(strip_discord_markup(text))

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


def pick_reply_simple() -> str:
    candidates: list[str] = [
        r for r in RESPONSES if r not in _last_replies
    ] or RESPONSES
    reply: str = random.choice(candidates)
    _last_replies.append(reply)
    return reply


def reply_dispatch(text: str) -> str | None:
    if contains_truth_question(text):
        return pick_reply_simple()


def should_reply(message: Message, user: ClientUser | None) -> bool:
    if user is None:
        return False
    else:
        if message.author == user:
            return False
        return (
            user.mentioned_in(message)
            or "@grok" in message.content.lower()
        )
