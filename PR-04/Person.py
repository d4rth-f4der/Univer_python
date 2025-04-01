# інструмент для створення абстрактних методів
from abc import ABC, abstractmethod

# створення абстрактного класу Person
class Person(ABC):
    #ініціалізація класу
    def __init__(self, name, age, prac_score, prac_count, exam_scr):
        self.name = name
        self.age = age
        self.prac_score = prac_score  # сумарний бал за практичні
        self.prac_count = prac_count  # кількість практичних
        self.exam_scr = exam_scr  # бал за іспит

    def avg_practice_score(self):       # метод розрахунку середнього балу за практичні
        if self.prac_count != 0:
            avg_prac = self.prac_score / self.prac_count
        else:
            avg_prac = 0
        return avg_prac