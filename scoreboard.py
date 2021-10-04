from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.display_score()
        self.hideturtle()
        self.setposition(0, 250)
        self.penup()

    def display_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", move=False, align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.display_score()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(-100,0)
        self.write(f"GAME OVER", move=False, align="left", font=FONT)