COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random
class CarManager():
    def __init__(self):
        self.clist = []
        self.speedcar = STARTING_MOVE_DISTANCE

    def createcar(self):
        num = random.randint(1,6)
        if num == 1:
            newcar = Turtle()
            newcar.color(random.choice(COLORS))
            newcar.shape("square")
            newcar.shapesize(stretch_wid=1, stretch_len=2)
            newcar.penup()
            newcar.goto(300, random.randint(-250,250))
            self.clist.append(newcar)

    def move(self):

        for car in self.clist:
            car.backward(self.speedcar)

    def levelupspeed(self):
        self.speedcar += MOVE_INCREMENT




