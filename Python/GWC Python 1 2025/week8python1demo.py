import turtle

jeff = turtle.Turtle()

screen = turtle.Screen()

# draw boundary box
boxOutline = turtle.Turtle()
boxOutline.speed(0)
boxOutline.color("red")

boxOutline.penup()
boxOutline.goto(-100, 100)
boxOutline.pendown()

for i in range(4):
  boxOutline.forward(200)
  boxOutline.right(90)

boxOutline.hideturtle()

# function for keyboard
def turnLeft():
  jeff.left(10)

def turnRight():
  jeff.right(10)
  
# bind keyboard and functions
screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.listen()

# score
score = 0
scoreTurtle = turtle.Turtle()
scoreTurtle.speed(1000)

scoreTurtle.penup()
scoreTurtle.goto(-100, 110)
scoreTurtle.pendown()

scoreTurtle.write("Score: " + str(score))
scoreTurtle.hideturtle()

# main loop
jeff.color("green")
jeff.goto(0, 0)
jeff.pendown()
jeff.speed(5)

while True:
  jeff.forward(2)
  
  if jeff.xcor() > 100 or jeff.xcor() < -100 or jeff.ycor() > 100 or jeff.ycor() < -100:
    jeff.write("Out of bounds!")
    break
    
  else:
    score += 1
    scoreTurtle.clear()
    scoreTurtle.write("Score: " + str(score))

turtle.done()