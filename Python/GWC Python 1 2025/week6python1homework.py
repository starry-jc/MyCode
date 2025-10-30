# importing modules
import turtle
import random

turtle.colormode(255)

# screen
s = turtle.Screen()
s.bgcolor("black")

# make it user interactive
numBranches = int(input("How many branches do you want the starburst to have? "))
numLongBranches = int(input("Every _ branches, the long will show: "))

# defining the function
# no arguments b/c they are user interactive 
def drawStarburst():
  # turtle + variables to make life easy
  starburst = turtle.Turtle()
  starburst.hideturtle()
  starburst.speed(0)
  starburst.pensize(2)
  starburst.goto(0, 0)
  turn = 360 / numBranches
  
  # for loop to draw the starburst
  for i in range(numBranches):
    # if modulus i by numLongBranches is 0...
    if i % numLongBranches == 0:
      # ...draw a long branch; otherwise,...
      starburst.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      starburst.forward(50)
      starburst.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      starburst.forward(50)
    else:
      # ...draw a short branch!
      starburst.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      starburst.forward(50)
      starburst.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
      starburst.forward(25)
    
    # resetting the location of turtle
    starburst.penup()
    starburst.goto(0, 0)
    starburst.pendown()
    starburst.right(turn)
  
# calling the function   
drawStarburst()

turtle.done()