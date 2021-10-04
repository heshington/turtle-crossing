from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    #create turtle player that starts at the bottom of the screen and listens for the up key.
    #
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setposition(0, -280)
        self.right(270)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_finished(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False




