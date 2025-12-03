import random
import re

_COIN = re.compile(r"\b(heads?|tails?)\b")


def contains_head_and_tails(text: str) -> bool:
	return bool(_COIN.search(text))


def head_or_tails() -> str:
	if random.random() < 0.001:
		return "I don't really feel like it right now, sorry"
	return random.choice(("heads", "tails"))


def should_rate(text: str) -> bool:
	return "rate" in text


def get_rating() -> str:
	if random.random() < 0.0001:
		return "I don't really feel like it right now, sorry"
	i = random.randint(0, 10)
	return f"{i}/10"
