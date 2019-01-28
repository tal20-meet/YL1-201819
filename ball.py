from turtle import *
import random
import turtle
turtle.colormode(255)
class Ball(Turtle):
    def __init__(self, x, y, dx, dy, r, color):
        self.dx = dx
        self.dy = dy
        self.r = r
        self.x = x
        self.y = y
        Turtle.__init__(self)
        self.penup()
        self.goto(x,y)
        self.shape('circle')
        self.shapesize(r/10)
        self.color(color)
    def move(self, screen_width, screen_height):
        current_x = self.xcor()
        new_x = current_x + self.dx
        current_y = self.ycor()
        new_y = current_y +  self.dy
        
        right_side_ball = new_x + self.r
        bottom_side_ball = new_y - self.r
        left_side_ball = new_x - self.r
        top_side_ball = new_y + self.r
        self.goto(new_x, new_y)
        
        check_col_width = left_side_ball <= -screen_width or right_side_ball >= screen_width
        check_col_height = top_side_ball >= screen_height or bottom_side_ball <= -screen_height
        if (check_col_width):
            self.dx = -self.dx
        elif (check_col_height):
            self.dy = -self.dy
    def new_Ball(self, x, y, dx, dy, r, color):
        self.dx = dx
        self.dy = dy
        self.r = r
        self.penup()
        self.goto(x,y)
        self.shape('circle')
        self.shapesize(r/10)
        self.color(color)
        
            
            
        
        
        
