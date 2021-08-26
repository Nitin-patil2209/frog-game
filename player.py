STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def Move(self):
        xcord = self.xcor()
        ycord = self.ycor() + MOVE_DISTANCE
        self.goto(xcord, ycord)

    def startingpos(self):
        self.goto(STARTING_POSITION)


