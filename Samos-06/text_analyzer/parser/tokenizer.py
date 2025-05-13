# Обробка рядків: розбиття на слова, очищення
import sys

from .. import config  # Імпорт набору роздільників
import string

def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
        print("Попередження: Функція tokenize отримала ввод, що не є рядком.", file=sys.stderr)
        return []

    tokens = []
    current_token_chars = []

    custom_delimiters = config.DELIMITERS

    for char in text:
        if char in custom_delimiters:
            if current_token_chars:
                token_str = "".join(current_token_chars)
                tokens.append(token_str)
                current_token_chars = []
        else:
            current_token_chars.append(char)

    if current_token_chars:
        token_str = "".join(current_token_chars)
        tokens.append(token_str)

    cleaned_tokens = []
    chars_to_strip = string.punctuation + string.whitespace

    for token in tokens:
        cleaned_token = token.strip(chars_to_strip)

        if cleaned_token:
            cleaned_tokens.append(cleaned_token)

    return cleaned_tokens