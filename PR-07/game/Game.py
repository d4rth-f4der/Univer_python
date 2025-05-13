from config import *
from Player import Player
from Target import Target

class Game:
    def __init__(self):
        self.target = None
        self.player = None
        self.tk = tk.Tk()
        self.tk.title("Дістанься до цілі")
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost", 1)

        self.canvas = tk.Canvas(self.tk, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg=COLOR_BG)
        self.canvas.pack()
        self.tk.update()
        self.running = True

        self.create_game_objects()
        self.tk.update()
        self.running = True

    def create_game_objects(self):
        # Створення гравця
        self.player = Player(self.canvas, 50, 50, 20, 30, "red")
        self.tk.bind("<KeyPress-Up>", self.player.move_up)
        self.tk.bind("<KeyPress-Down>", self.player.move_down)
        self.tk.bind("<KeyPress-Left>", self.player.move_left)
        self.tk.bind("<KeyPress-Right>", self.player.move_right)
        # Створення цілі
        self.target = Target(self.canvas, 15, "green")

    def mainloop(self):
        while self.running:  # Поки гра активна
            self.player.move()  # Викликає метод move об'єкта player
            # Перевіряє зіткнення між гравцем та ціллю
            self.check_collisions()
            self.tk.update_idletasks()  # Оновлює інтерфейс користувача
            self.tk.update()  # Оновлює вікно Tkinter
            time.sleep(0.01)

    def check_collisions(self):
        # Перевірка зіткнення гравця з ціллю
        if self.player.collides_with(self.target):
            print("Гра виграна!")
            self.running = False


