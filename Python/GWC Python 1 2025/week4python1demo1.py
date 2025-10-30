import turtle
import random

bob = turtle.Turtle()
turtle.colormode(255)

red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)

bob.color(red, green, blue)
bob.shape("turtle")

sides = 6
angle = 360 / sides

for i in range(sides):
  bob.forward(100)
  bob.right(angle)

turtle.done()