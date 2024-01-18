#Turtle:

import turtle
x=turtle.Turtle()
turtle.bgcolor("black")
x.pensize(2)
x.color("yellow")
j=10
for i in range(10):
    x.circle(j)
    j=j+5
