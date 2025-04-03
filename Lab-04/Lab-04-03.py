def evaluate_expression(expression):
    expression = expression.strip()
    if expression.startswith('(') and expression.endswith(')'):
        expression = expression[1:-1].strip()
        balance = 0
        operator_index = -1
        operator = None
        for i in range(len(expression)):
            char = expression[i]
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
            elif balance == 0 and char in ['+', '-', '*', '/']:
                operator_index = i
                operator = char
                break

        if operator:
            left_operand = expression[:operator_index].strip()
            right_operand = expression[operator_index + 1:].strip()
            left_value = evaluate_expression(left_operand)
            right_value = evaluate_expression(right_operand)
            if operator == '+':
                return left_value + right_value
            elif operator == '-':
                return left_value - right_value
            elif operator == '*':
                return left_value * right_value
            elif operator == '/':
                if right_value == 0:
                    raise ZeroDivisionError("Ділення на нуль")
                return left_value / right_value

    try:
        return float(expression)
    except ValueError:
        raise ValueError(f"Неправильний формат виразу: {expression}")

print("Введіть арифметичний вираз частинами (дужку, оператор або число).\n"
      "КОЖЕН ВИРАЗ МАЄ БУТИ В ДУЖКАХ!")
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