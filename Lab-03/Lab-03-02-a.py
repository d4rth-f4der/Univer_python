# Лабораторна 3 завдання 2 (a)

def f(x):
    try:
        return int(1 / x)   # І виклик кине помилку ZeroDivisionError; ІІ виклик ділить, але не повертає із-за return в finally
    except TypeError:   # не опрацьовує ZeroDivisionError, вона буде опрацьована після виконання функції
        print(1, end="")
    else:
        print(2, end="")
        return 0
    finally:
        print(3, end="")    # І виклик друкує 3; IІ виклик друкує 3
        return 2    # І виклик повертає 2, перекриває ZeroDivisionError; ІI виклик повертає 2

try:
    print(f(0), end="") # друкує 2
    print(f(1), end="") # друкує 2
except:
    print(4, end="")