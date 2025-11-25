import re
import string

_PUNCT = string.punctuation.replace("?", "")

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


def strip_discord_markup(text: str) -> str:
    return _DISCORD_MARKUP.sub(" ", text)


def normalize(text: str) -> str:
    text = text.lower()
    # remove punctuation besides ? marks
    for p in _PUNCT:
        text = text.replace(p, " ")
    return " ".join(text.split())
