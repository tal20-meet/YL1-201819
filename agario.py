import turtle
import time
import random
import math
from ball import Ball
turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()
#Part 1
global running
running = True
global screen_width
screen_width = turtle.getcanvas().winfo_width()/2
global screen_height
screen_height = turtle.getcanvas().winfo_height()/2

my_ball=Ball(0, 0, 0, 0, 50, 'red')

number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5

BALLS = []
for i in range(number_of_balls):
    new_ball_x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
    new_ball_y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
    new_ball_dx = random.randint(minimum_ball_dx, maximum_ball_dx)
    new_ball_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
    new_ball_r =random.randint(minimum_ball_radius,maximum_ball_radius)
    new_ball_color = (random.random(), random.random(), random.random())
    
    new_ball = Ball(new_ball_x, new_ball_y, new_ball_dx, new_ball_dy, new_ball_r, new_ball_color)
    BALLS.append(new_ball)  

def move_all_balls():
    for ball in BALLS:
        ball.move(screen_width, screen_height)


def collide(ball_a, ball_b):
    if ball_a == ball_b:
        return False
    d = math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor()),2)+ math.pow((ball_a.ycor()-ball_b.ycor()), 2))
    if (ball_a.r+ ball_b.r>=d):
        return True
    else:
        return False
turtle.update()


def check_all_balls_collision():
    all_balls=[]
    all_balls.append(my_ball)
    for ball in BALLS:
        all_balls.append(ball)
    for ball_a in all_balls:
        for ball_b in all_balls:
            if collide(ball_a, ball_b):
                r1 = ball_a.r
                r2 = ball_b.r
                x = random.randint(-screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
                y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
                dx = random.randint(minimum_ball_dx, maximum_ball_dx)
                dy = random.randint(minimum_ball_dy,maximum_ball_dy)
                r = random.randint(minimum_ball_radius,maximum_ball_radius)
                color = (random.random(), random.random(), random.random())
                while dx == 0:
                    dx = random.randint(minimum_ball_dx, maximum_ball_dx)
                while dy == 0:
                    dy = random.randint(minimum_ball_dy,maximum_ball_dy)
                    
                if r1<r2:
                    if ball_a == my_ball:
                        print("game over")
                        quit()
                    else:
                        my_ball.r += 2
                        ball_b.shapesize(ball_b.r/10)
                        ball_a.new_Ball(x, y, dx, dy, r, color)
                else:
                    if ball_b == my_ball:
                        print("game over")
                        quit()
                    else:
                        ball_a.r += 1
                        ball_a.shapesize(ball_a.r/10)
                        ball_b.new_Ball(x, y, dx, dy, r, color)
            if ball_a.r > 200 and not(ball_a == my_ball):
                print("you lose!!!")
                quit()
            elif my_ball.r>200:
                print("you win!!!")
                quit()
                
   
def movearound():
    my_ball.goto(turtle.getcanvas().winfo_pointerx()- screen_width, screen_height - turtle.getcanvas().winfo_pointery())
    if my_ball.x<screen_width - my_ball.r and my_ball.x > screen_width + my_ball.r:
        my_ball.goto(my_ball.x, my_ball.y)
    
while running is True:
    screen_width = turtle.getcanvas().winfo_width()/2
    screen_height = turtle.getcanvas().winfo_height()/2
    movearound()
    move_all_balls()
    check_all_balls_collision()
    time.sleep(.1)
    turtle.update()
turtle.update()
turtle.mainloop() 














    

        
    
