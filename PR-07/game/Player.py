from config import *

class Player:
    def __init__(self, canvas, x, y, width, height, color):
        self.canvas = canvas  # Зберігає посилання на полотно, на якому буде зображений гравець
        self.id = canvas.create_rectangle(x, y, x + width, y + height, fill=color)
        self.vx = 0  # Швидкість гравця по горизонталі (початково 0)
        self.vy = 0  # Швидкість гравця по вертикалі (початково 0)

    def move(self):
        co = self.canvas.coords(self.id)  # Отримує поточні координати гравця
        # Перевіряє, чи гравець не виходить за межі вікна по горизонталі
        if co[0] + self.vx < 0 or co[2] + self.vx > SCREEN_WIDTH:
            self.vx = 0  # Якщо так, обнуляє горизонтальну швидкість
        # Аналогічна перевірка для вертикального руху
        if co[1] + self.vy < 0 or co[3] + self.vy > SCREEN_HEIGHT:
            self.vy = 0  # Обнуляє вертикальну швидкість, якщо гравець виходить за межі
        self.canvas.move(self.id, self.vx, self.vy)  # Рухає гравця на відстань (vx, vy)

    def move_up(self, event):
        # для руху вгору
        self.vy = -2

    def move_down(self, event):
        # для руху вниз
        self.vy = 2

    def move_left(self, event):
        # для руху вліво
        self.vx = -2

    def move_right(self, event):
        # для руху вправо
        self.vx = 2

    def collides_with(self, sprite):  # перевіряє зіткнення гравця з іншим об'єктом
        # Отримує поточні координати гравця на полотні
        pos = self.canvas.coords(self.id)

        # Знаходить усі об'єкти на полотні, які перетинаються з гравцем
        overlap = self.canvas.find_overlapping(*pos)

        # Перевіряє, чи ID переданого об'єкта (sprite) знаходиться серед перетинаючихся об'єктів
        return sprite.id in overlap
