import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.pendown()

# pick your own color?
color = input("What color do you want your snowflake to be? ")

def draw_branch():
  t.goto(0, 0)
  t.color(color)
  
  for i in range(10):
    t.forward(10)
    
    t.right(45)
    t.forward(20)
    t.backward(20)
    
    t.left(90)
    t.forward(20)
    t.backward(20)
    t.right(45)
    
  t.right(60)

for i in range(6):
  draw_branch()

turtle.done()