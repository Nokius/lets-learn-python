import turtle

a = 100

def draw_hex(length):
    for _ in range(6):
        turtle.forward(length)
        turtle.left(60)

for _ in range(6):
    draw_hex(a)
    turtle.forward(a)
    turtle.right(60)

turtle.exitonclick()
