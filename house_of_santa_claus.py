import turtle
import math

a = b = 20

c = math.sqrt(a**2 + b**2)

turtle.forward(c)
turtle.left(135)
turtle.forward(b)
turtle.left(90)
turtle.forward(a)

turtle.exitonclock()

