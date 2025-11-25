import random


def contains_head_and_tails(text: str) -> bool:
    return "head" in text and "tails" in text


def head_or_tails() -> str:
    return random.choice(("head", "tails"))


def should_rate(text: str) -> bool:
    return "rate" in text


def get_rating() -> str:
    i = random.randint(0, 10)
    return f"{i}/10"
