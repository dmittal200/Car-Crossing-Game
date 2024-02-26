from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_all=[]
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        randm_num = random.randint(1,6)
        if randm_num==1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            new_y = random.randint(-300, 300)
            car.goto(290, new_y)
            self.car_all.append(car)

    def move(self):
        for cars in self.car_all:
            cars.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
