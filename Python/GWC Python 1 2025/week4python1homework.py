# importing modules
import turtle
import random

turtle.colormode(255)

# variables
rows = 2
columns = 2
shape_size = 50

# setting up the squares turtle
squares = turtle.Turtle()
squares.penup()
squares.goto(-50, 50)
squares.pendown()

# squares nested for loop
for i in range(rows):
  for j in range(columns):
    # start with a splash of color!
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    squares.fillcolor(red, green, blue)
    squares.pencolor(red, green, blue)
    
    # drawing the square
    squares.begin_fill()
    for k in range(4):
      squares.forward(shape_size)
      squares.right(90)
    squares.end_fill()
    
    # moving toward the next area
    squares.penup()
    squares.forward(shape_size + 5)
    squares.pendown()
    # end of loop
  
  # moving to the next row
  squares.penup()
  squares.goto(-50, 50 - (i + 1) * (shape_size + 5))
  squares.pendown()
  # end of loop

# setting up triangles turtle
triangles = turtle.Turtle()
triangles.penup()
triangles.goto(-50, 50)
triangles.pendown()

# triangles nested while loop (challenge!)
rows = 0

while rows < 2:
  columns = 0
  
  while columns < 2:
    # start with a splash of color!
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    triangles.fillcolor(red, green, blue)
    triangles.pencolor(red, green, blue)
    
    # drawing the triangle
    x = 0
    triangles.begin_fill()
    while x < 3:
      triangles.forward(shape_size)
      triangles.right(120)
      x += 1
    triangles.end_fill()
    
    # moving toward the next area
    triangles.penup()
    triangles.forward(shape_size + 5)
    triangles.pendown()
    
    columns += 1
    # end of loop
  
  # moving to the next row
  triangles.penup()
  triangles.goto(-50, 50 - (rows + 1) * (shape_size + 5))
  triangles.pendown()
  
  rows += 1
  # end of loop

turtle.done()