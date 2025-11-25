import random


def contains_head_and_tails(text: str) -> bool:
    return "head" in text and "tails" in text


def head_or_tails() -> str:
    return random.choice(("head", "tails"))
