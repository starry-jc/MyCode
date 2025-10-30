import turtle
import random

turtle.colormode(255)

lacey = turtle.Turtle()
lacey.penup()
lacey.goto(-75, 75)
lacey.pendown()

'''red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)'''

rows = 3
columns = 3
square_size = 50

for i in range(rows):
  for j in range(columns):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    lacey.fillcolor(red, green, blue)
    
    lacey.begin_fill()
    for k in range(4):
      lacey.forward(square_size)
      lacey.right(90)
    lacey.end_fill()
    
    lacey.penup()
    lacey.forward(square_size + 5)
    lacey.pendown()
  
  lacey.penup()
  lacey.goto(-75, 75 - (i + 1) * (square_size + 5))
  lacey.pendown()

turtle.done()