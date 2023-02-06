from turtle import Turtle
FONT = ("Arial", 24, "normal")


class Levels(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.color("white")
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.goto(0, 270)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!!", move=False, align="center", font=FONT)