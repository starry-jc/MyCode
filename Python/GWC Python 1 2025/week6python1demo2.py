# importing modules
import turtle

turtle.colormode(255)

# screen settings (white bg is gross to look at a neon yellow star)
s = turtle.Screen()
s.bgcolor("black")

# turtle settings
starryNight = turtle.Turtle()
starryNight.hideturtle()
starryNight.penup()
starryNight.goto(-144, 0)
starryNight.speed(0)
starryNight.pendown()

# making the function
def drawStar(color):
  # giving it color
  starryNight.color(color)
  starryNight.fillcolor(color)
  starryNight.begin_fill()
  
  # for loop to draw and color the star
  for i in range(5):
    starryNight.forward(144 * 2)
    starryNight.right(72 * 2)
    
  starryNight.end_fill()

# summoning the star
drawStar("yellow")

turtle.done()