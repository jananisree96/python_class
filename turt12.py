#turtle:

import turtle
t=turtle.Turtle()
t.pensize(2)
a=20
c=["red","blue","yellow","green","black"]
for j in c:
    x=1
    for i in range(x):
        t.color(j)
        t.circle(a)
        a=a+10
        
