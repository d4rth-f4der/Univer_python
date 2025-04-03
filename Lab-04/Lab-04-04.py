def precedence(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    return 0

def apply_op(left, operator, right):
    if operator == '+':
        return left + right
    elif operator == '-':
        return left - right
    elif operator == '*':
        return left * right
    elif operator == '/':
        if right == 0:
            raise ZeroDivisionError("Ділення на нуль")
        return left / right
    return 0

def evaluate_expression(expression):
    expression = expression.strip()

    def evaluate(tokens):
        if not tokens:
            raise ValueError("Порожній вираз")
        if len(tokens) == 1:
            try:
                return float(tokens[0])
            except ValueError:
                raise ValueError(f"Неправильний формат токена: {tokens[0]}")

        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] in ('+', '-'):
                return apply_op(evaluate(tokens[:i]), tokens[i], evaluate(tokens[i+1:]))

        for i in range(len(tokens) - 1, -1, -1):
            if tokens[i] in ('*', '/'):
                return apply_op(evaluate(tokens[:i]), tokens[i], evaluate(tokens[i+1:]))

        if tokens[0] == '(' and tokens[-1] == ')':
            balance = 0
            enclosed = True
            for i in range(len(tokens)):
                if tokens[i] == '(':
                    balance += 1
                elif tokens[i] == ')':
                    balance -= 1
                if balance == 0 and i < len(tokens) - 1:
                    enclosed = False
                    break
            if enclosed:
                return evaluate(tokens[1:-1])

        raise ValueError(f"Неправильний формат виразу: {' '.join(tokens)}")

    tokens = []
    current_number = ""
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        elif char in ('+', '-', '*', '/', '(', ')'):
            if current_number:
                tokens.append(current_number)
                current_number = ""
            tokens.append(char)
        elif char == ' ':
            if current_number:
                tokens.append(current_number)
                current_number = ""
        else:
            raise ValueError(f"Недопустимий символ у виразі: {char}")
    if current_number:
        tokens.append(current_number)

    return evaluate(tokens)

print("Введіть арифметичний вираз частинами (дужку, оператор або число).")
print("Для завершення введіть '='.")

expression_parts = []
while True:
    part = input("> ")
    if part == '=':
        break
    expression_parts.append(part)

full_expression = "".join(expression_parts)
print(f"Повний вираз: {full_expression}")

try:
    result = evaluate_expression(full_expression)
    print(f"Результат: {result}")
except ValueError as e:
    print(f"Помилка: {e}")
except ZeroDivisionError as e:
    print(f"Помилка: {e}")
except Exception as e:
    print(f"Виникла непередбачена помилка: {e}")