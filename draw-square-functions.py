import turtle

def squer(length, angle):
    turtle.forward(length)
    turtle.left(angle)

for _ in range(4):
    squer(100, 90)

turtle.exitonclick()
