from turtle import *
import random
import math

class ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball1 = ball(5, "red", 100)
ball2 = ball(5, "blue", 99)
ball1.goto(0,0)
ball2.goto(10,0)
ball_list = (ball,ball2)

def check_collision(ball1, ball2):
    r1 = ball1.radius
    r2 = ball2.radius
    x1 = ball1.pos()[0]
    y1 = ball1.pos()[1]
    x2 = ball2.pos()[0]
    y2 = ball2.pos()[1]
    d = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    r_sum = r1 + r2
    if r_sum>=d :
        print('collision!!!')
    else:
        print('no collision')
check_collision(ball1, ball2)

mainloop()
