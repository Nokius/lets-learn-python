import turtle

def hex_wing():
    for _ in range(6):
        turtle.forward(50)
        turtle.left(60)

for _ in range(1):
    hex_wing()
    turtle.forward(50)
    turtle.right(60)

turtle.exitonclick()
