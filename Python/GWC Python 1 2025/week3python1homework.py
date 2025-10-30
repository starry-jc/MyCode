# importing turtle module
import turtle

turtle.colormode(255)

# defining + drawing turtle1
turtle1 = turtle.Turtle()   # use a for loop

turtle1.penup()
turtle1.goto(-100, 0)
turtle1.pendown()

turtle1.fillcolor("pink")
turtle1.begin_fill()

for i in range(3):
  turtle1.forward(100)
  turtle1.right(120)

turtle1.end_fill()

# defining + drawing turtle2
turtle2 = turtle.Turtle()   # use a while loop
i = 0

turtle2.penup()
turtle2.goto(100, 0)
turtle2.pendown()

turtle2.fillcolor(144, 60, 163)
turtle2.begin_fill()

while i < 3:
  turtle2.forward(100)
  turtle2.left(120)
  i += 1
  
turtle2.end_fill()

turtle.done()