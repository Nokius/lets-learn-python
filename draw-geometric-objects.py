import turtle

def draw_object(length, edges):
    for _ in range(edges):
        turtle.forward(length)
        turtle.left( 360 / edges)

for _ in range(1):
    draw_object(50, 1)

turtle.exitonclick()
