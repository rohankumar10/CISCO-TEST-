import turtle

# Initalize the turtle library so we can use it safely
turtle1 = turtle.Turtle()

turtle1.up()
turtle1.goto(-50, 0)
turtle1.down()


def draw_square():
    # Since we need the square to at an angle 90  
    turtle1.left(50)
    # FOR LOOP to make 4 sides of square
    for _ in range(4):
        turtle1.forward(150)
        turtle1.left(90)
    turtle1.up()
    turtle1.right(50)

def draw_circle():
    # Moving to coordinates so we can circle the above square
    turtle1.goto(-50, -50)
    turtle1.down()
    turtle1.circle(150, 360)
    turtle1.up()

def draw_hexagon():
    # Moving to coordinates so we can draw outside the boundary of circle
    turtle1.goto(50, -100)
    turtle1.down()
    # FOR LOOP to make 6 sides of hexagon
    for _ in range(6):
        turtle1.left(360/6)
        turtle1.fd(1250/6)
    turtle1.up()

draw_square()
draw_circle()
draw_hexagon()
turtle1.done()