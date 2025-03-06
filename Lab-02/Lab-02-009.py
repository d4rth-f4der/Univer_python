# Лабораторна 2 завдання 9
import math

def math_module():
    while True:
        action = input("""
        Виберіть математичну функцію
        s - квадратний корінь
        log - логарифм
        sin - синус
        cos - косинус
        tan - тангенс
        fact - факторіал
        exp - піднесення е у степінь
        q - вийти: 
        """)
        if action.lower() == 's':
            a = int(input("Введіть ціле число: "))
            print(f'\u221A{a} = {math.sqrt(a)}')
        if action.lower() == 'log':
            base = int(input("Введіть основу логарифма: "))
            a = int(input("Введіть логарифмоване число: "))
            print(f'log(base {base}){a} = {math.log(a, base)}')
        if action.lower() == 'sin':
            x = int(input("Введіть ціле число: "))
            print(f'sin({x}) = {math.sin(x)}')
        if action.lower() == 'cos':
            x = int(input("Введіть ціле число: "))
            print(f'cos({x}) = {math.cos(x)}')
        if action.lower() == 'tan':
            x = int(input("Введіть ціле число: "))
            print(f'tg({x}) = {math.tan(x)}')
        if action.lower() == 'fact':
            x = int(input("Введіть ціле число: "))
            print(f'{x}! = {math.factorial(x)}')
        if action.lower() == 'exp':
            x = int(input("Введіть ступінь експоненти: "))
            print(f'е^{x} = {math.exp(x)}')
        if action.lower() == 'q': break

math_module()