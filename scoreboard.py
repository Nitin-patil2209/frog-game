FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.updato()

    def updato(self):
        self.goto(180,260)
        self.write(f"Level {self.score}", align="center", font=FONT)

    def upscore(self):
        self.clear()
        self.score += 1
        self.write(f"Level {self.score}", align="center", font=FONT)

    def gameover(self):
        self.clear()
        self.write("Game Over", align="center", font=FONT)

