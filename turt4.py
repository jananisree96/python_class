import turtle

# Function to draw a petal
def draw_petal():
    turtle.circle(50, 60)
    turtle.left(120)
    turtle.circle(50, 60)
    turtle.left(120)

# Function to draw a rose
def draw_rose():
    for _ in range(6):
        draw_petal()
        turtle.left(60)

# Set up the turtle
turtle.speed(2)

# Draw the rose
draw_rose()

# Hide the turtle
turtle.hideturtle()

# Keep the window open
turtle.done()
