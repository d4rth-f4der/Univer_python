from tkinter import *
from Score import Score
from Catcher import Catcher
from Egg import Egg
import random
import time

tk = Tk()
tk.title("Гра: Ловець!")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

score = Score(canvas)
catcher = Catcher(canvas, 'blue', score)
eggs = []

while 1:  # Початок нескінченного циклу для ігрового процесу
    if random.randint(1, 100) == 1:  # Випадкова перевірка (1% шанс)
        eggs.append(Egg(canvas, 'red', score))  # Створення нового яйця та додавання до списку
    for egg in list(eggs):  # Ітерація по копії списку яєць
        if egg.draw() == 'hit bottom':
            eggs.remove(egg)  # Якщо яйце досягло дна - видаляємо
    catcher.catch(eggs)
    catcher.draw()
    tk.update_idletasks()  # Оновлення ігрового інтерфейсу без блокування інших завдань
    tk.update()  # Повне оновлення всього ігрового вікна
    time.sleep(0.01)  # Коротка пауза
    if score.lost >= 5:
        break

canvas.create_text(250, 200, text="Гра завершена!", font=('Helvetica', 30), fill='red')
canvas.create_text(250, 250, text=f"Ви пропустили {score.lost} яєць.", font=('Helvetica', 20), fill='red')

tk.update()
time.sleep(3)