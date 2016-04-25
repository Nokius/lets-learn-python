import turtle


def move():
    direction = input("Go left or right? ")
    direction = direction.strip().lower()
    if direction == "left":
        turtle.left(60)
        turtle.forward(50)
    if direction == "right":
        turtle.right(60)
        turtle.forward(50)

for _ in range(10):
    move()

#turtle.exitonclick()
