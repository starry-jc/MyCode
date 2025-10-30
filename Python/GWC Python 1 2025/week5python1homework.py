# import modules
import random
import turtle

turtle.colormode(255)

# friendly welcome message :)
print("Welcome to shape selector!")

# starting the shape selecting loop
x = 0
while x < 2:
  # setting up the input
  shapeSelect = int(input("Please select a number from 0-2 ({}/2)".format(x + 1)))
  
  # conditionals
  if shapeSelect == 0:
    # create triangle turtle
    triangle = turtle.Turtle()
    triangle.penup()
    triangle.goto(-50, 0)
    triangle.pendown()
    
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    triangle.pencolor(red, green, blue)
    triangle.pensize(5)
    
    # while loop to draw triangle
    y = 0
    while y < 3:
      triangle.forward(100)
      triangle.right(120)
      
      # ending the loop
      y += 1
    
  elif shapeSelect == 1:
    # create circle turtle
    circle = turtle.Turtle()
    circle.penup()
    circle.goto(100, 0)
    circle.pendown()
    
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    circle.pencolor(red, green, blue)
    circle.pensize(5)
    
    # draw circle
    circle.circle(50)
    
  elif shapeSelect == 2:
    # create square turtle
    square = turtle.Turtle()
    square.penup()
    square.goto(50, -50)
    square.pendown()
    
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    square.pencolor(red, green, blue)
    square.pensize(5)
    
    # while loop to draw square
    z = 0
    while z < 4:
      square.forward(100)
      square.right(90)
      
      # ending the loop
      z += 1
      
    # how to deal with trolls
  else:
    print("Invalid input! Please try again.")
    break
  
  # ending the loop
  x += 1

turtle.done()