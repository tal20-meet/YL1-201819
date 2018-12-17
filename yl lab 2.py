import tkinter as tk
from tkinter import simpledialog

#exercise 1
def new_list():
    a = [5,6,7,8,9]
    b = [a[1],a[-1]]
    print(b)
new_list()
#exercise 2
a = [1,3,6,8,34,6,4,2,3,1]
c=[]
for i in a:
    if(i<5):
        #print(i)
        c.append(i)
print(c)

#exercise 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a:
    for s in b:
        if (i==s):
            c.append(i)
print(c)    

def ok(a):
    for i in range(2, a/2):
        if a%1==0:
            return Faulse
    return True
print(ok(input('khs')))

from turtle import *
import random

class Square(Turtle):
    def __init__(self, size, color):
        Turtle.__init__(self)
        self.size = size
        self.shape("square")
        self.shapesize(size)
        self.color(color)
        
    def random_color():
        color = random.choice(['red' , 'orange' , 'yellow' , 'blue' , 'green' , 'pink'])
        
s1 = Square(5, color)

