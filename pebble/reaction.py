import re

from main import DEBUG

# stores the mapping of pattern -> emoji reactions
_RAW_REACTION_MAP: dict[str, str] = {
	r"smok": "<:ramoke:1310422073562365972>",
	r"\bgnu(\+|/)linux\b": "🐧",
	r"\bblazing(ly)?\s+fast\b": "🦀",
	r"\bhom(o|ie)sexual\b": "🏳️‍🌈",
	r"\bwe\s+.*live\s+in\s+a\s+society\b": "🃏",
	r"\ba\s+monad\s+is\s+just\s+a\s+monoid\s+in\s+the\s+category\s+of\s+endofunctors\b": "📦",
	r"\bthere\s+are\s+no\s+bugs,\s+only\s+undocumented\s+features\b": "🐛",
	r"\bposix\s+(sh\s+)?is\s+my\s+love\s+language\b": "❤️",
	r"\bimpressive,?\s+very\s+nice,?\s+now\s+let'?s\s+see\s+paul\s+allen'?s\s+\w+\b": "🪪",
	r"\bpatrick\s+bateman\b": "🪪",
}
if DEBUG:
	_RAW_REACTION_MAP[r"unicode"] = "👍"
	_RAW_REACTION_MAP[r"skibidi"] = "<:SKIBIDI:1425551738370396301>"


# for a given MESSAGE, returns a list of emoji that should
# be added as reactions. List may be empty.
def reacts_with(s: str) -> list[str]:
	out: list[str] = []
	for k in _RAW_REACTION_MAP:
		if re.search(k, s.lower()):
			out.append(_RAW_REACTION_MAP[k])
	return out
