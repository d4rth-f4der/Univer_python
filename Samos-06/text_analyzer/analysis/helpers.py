# is_number, is_delimiter, тощо

def is_number(token: str) -> bool:
    if not token:
        return False

    if token[0] in ('+', '-'):
        token = token[1:] # Видаляємо опціональний знак на початку, якщо він є

    if not token:
        return False

    try:
        float(token)
        return True
    except ValueError:
        return False