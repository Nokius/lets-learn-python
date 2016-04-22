import turtle

for _ in range(4):
   turtle.forward(100)
   turtle.left(90)
   
   for _ in range(8):
      turtle.right(90)
      turtle.forward(10)

turtle.exitonclick()
