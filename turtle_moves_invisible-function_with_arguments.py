import turtle

def line_without_moving(length):
    turtle.forward(length)
    turtle.backward(length)

line_without_moving(50)

turtle.exitonclick()
