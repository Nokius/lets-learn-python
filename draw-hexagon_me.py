import turtle

def hex_wing():
    for _ in range(6):
        turtle.forward(50)
        turtle.left(60)

def hex_next():
    turtle.forward(50)
    turtle.right(60)

for _ in range(6):
    hex_wing()
    hex_next()

turtle.exitonclick()
