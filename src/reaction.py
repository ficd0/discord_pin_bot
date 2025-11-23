import re

_REACTION_MAP: dict[str, str] = {r"smok": "<:ramoke:1310422073562365972>"}


def reacts_with(s: str) -> list[str]:
    out: list[str] = []
    for k in _REACTION_MAP:
        if re.search(k, s):
            out.append(_REACTION_MAP[k])
    return out
