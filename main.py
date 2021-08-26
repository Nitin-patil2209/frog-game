import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

score = Scoreboard()
player = Player()
car = CarManager()



screen.onkey(player.Move, "Up")

game_is_on = True
while game_is_on:


    time.sleep(0.1)
    screen.update()
    car.createcar()
    car.move()
    for cari in car.clist:
        if player.distance(cari) < 20:
            game_is_on = False
            score.gameover()

    if player.ycor() == 290:
        score.upscore()
        car.levelupspeed()
        player.startingpos()



screen.exitonclick()