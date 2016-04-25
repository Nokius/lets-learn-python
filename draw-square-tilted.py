import turtle

def wing():
    turtle.left(20)
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)


for _ in range(20):
    wing()

turtle.exitonclick()
