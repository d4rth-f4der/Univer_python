num = 0

def f1(n):
    global num
    num += 1
    if n > 0:
        f1(n-1)

try:
    f1(2000)
except RecursionError as e:
    print(f"Було {num} викликів, і програма завершилася з помилкою.", e, sep="\n")
except BaseException:
    print("Щось пішло не так...")