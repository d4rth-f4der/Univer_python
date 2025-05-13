# Підрахунок чисел, знакозмін, інше

from . import helpers

def get_sign_category(number_str: str) -> str | None:
    if not helpers.is_number(number_str):
        return None

    try:
        num = float(number_str)
        if num > 0:
            return 'POS'
        elif num < 0:
            return 'NEG'
        else:
            return 'ZERO'
    except ValueError:
        return None

def count_digits(tokens: list[str]) -> int:
    return len([token for token in tokens if helpers.is_number(token)])

def alternation_count(tokens: list[str]) -> int:
    alternations = 0
    previous_sign_category = None

    for token in tokens:
        current_sign_category = get_sign_category(token)

        if current_sign_category is not None:
            if previous_sign_category is not None:
                if current_sign_category != previous_sign_category:
                    alternations += 1

            previous_sign_category = current_sign_category

    return alternations