import re

from main import DEBUG

# stores the mapping of pattern -> emoji reactions
_REACTION_MAP: dict[str, str] = {
    r"smok": "<:ramoke:1310422073562365972>",
    r"\bgnu(\+|/)linux\b": "🐧",
    r"\bblazing(ly)?.fast\b": "🦀",
    r"\bhom(o|ie)sexual\b": "🏳️‍🌈",
}
if DEBUG:
    _REACTION_MAP[r"unicode"] = "👍"
    _REACTION_MAP[r"skibidi"] = "<:SKIBIDI:1425551738370396301>"


# for a given MESSAGE, returns a list of emoji that should
# be added as reactions. List may be empty.
def reacts_with(s: str) -> list[str]:
    out: list[str] = []
    for k in _REACTION_MAP:
        if re.search(k, s.lower()):
            out.append(_REACTION_MAP[k])
    return out
