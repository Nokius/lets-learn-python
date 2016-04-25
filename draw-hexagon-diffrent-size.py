import turtle

def draw_hex(length):
    for _ in range(6):
        turtle.forward(length)
        turtle.left(60)

for _ in range(6):
    draw_hex(50)
    turtle.forward(50)
    turtle.right(60)

turtle.exitonclick()
