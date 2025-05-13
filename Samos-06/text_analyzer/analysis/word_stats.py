# Підрахунок слів, унікальність, довжини

from .. import config
import re

def count_words(tokens: list[str]) -> int:
    return len(tokens)

def count_words_len(tokens: list[str], n: int) -> int:
    return len([token for token in tokens if len(token) == n])

def count_unique_words(tokens: list[str]) -> int:
    if config.CASE_SENSITIVE:
        unique_tokens = set(tokens)
    else:
        unique_tokens = set(token.lower() for token in tokens)

    return len(unique_tokens)

def count_titlecase_words(tokens: list[str]) -> int:
    return len([token for token in tokens if token.istitle()])

def count_sentences(text: str) -> int:
    if not text or not text.strip():
        return 0

    # Регулярний вираз для пошуку кінця речення:
    # [.!?]     - шукаємо один з символів: крапка, знак оклику або знак питання
    # (\s|\Z)   - за яким слідує АБО один або більше пробільних символів (\s),
    #             АБО кінець всього рядка (\Z - якір кінця рядка)
    sentence_endings_pattern = r'[.!?](\s|\Z)'
    matches = re.findall(sentence_endings_pattern, text)
    count = len(matches)
    if count == 0 and len(text.strip()) > 0:
         return 1
    return count