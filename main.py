import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen = Screen()
screen.setup(width=600, height=600)

player = Player()
car = CarManager()
Score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()

    #detect collision with car
    for cars in car.car_all:
        if cars.distance(player)<20:
            game_is_on = False
            Score.game_over()

    #if the player finishes
    if player.is_at_finish_line()==True:
        player.go_to_start()
        car.level_up()
        Score.increase_level()

screen.exitonclick()




