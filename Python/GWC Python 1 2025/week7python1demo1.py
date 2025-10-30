import turtle

turtle.colormode(255)

# list of colors
colors = ["red", "coral", "orange", "yellow", "green", "cyan", "blue", "purple", "violet", "pink", "gray", "white"]

bob = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")

bob.speed(5)
bob.shape("turtle")
bob.pensize(10)

length = 0

for c in colors:
  if length % 90 == 0:
    bob.right(90)
  
  bob.color(c)
  bob.forward(30)
  length += 30

turtle.done()