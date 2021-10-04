from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.display_score()
        self.setposition(0, 250)
        self.penup()

    def display_score(self):
        self.write(f"Level: {self.score}", move=False, align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1

    def game_over(self):
        self.write(f"GAME OVER", move=False, align="left", font=FONT)