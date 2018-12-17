#problem 1
print('Tal'*100)

#problem 2
number1 = 4
print(number1)
number2 = number1/2
print(number2)

#problem 3
list1 = [2 , 3 , 4]
for i in list1:
	print(i)
	print(i * 2)
	
print(list1[0] + list1[1] + list1[2])

#problem 4
import turtle

turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.end_fill()

turtle.pensize(7)
turtle.penup()
turtle.goto(-35,30)
turtle.pendown()
turtle.color('blue')
turtle.circle(60)

turtle.penup()
turtle.goto(30,-30)
turtle.pendown()
turtle.color('yellow')
turtle.circle(60)

turtle.penup()
turtle.goto(95,30)
turtle.pendown()
turtle.color('black')
turtle.circle(60)

turtle.penup()
turtle.goto(160,-30)
turtle.pendown()
turtle.color('green')
turtle.circle(60)

turtle.penup()
turtle.goto(225,30)
turtle.pendown()
turtle.color('red')
turtle.circle(60)

turtle. mainloop()

