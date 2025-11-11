import turtle

s = turtle.Screen()
s.colormode(255)

# inputs
shape = input("Enter shape (circle/triangle): ").lower()
size = int(input("Enter size: "))

# create turtle
starberry = turtle.Turtle()

# if statement
if shape == "circle":
  if size > 50:
    starberry.pensize(5)
    if size > 100:
      starberry.pencolor("red")
    else:
      starberry.pencolor("blue")
  else:
    starberry.pensize(2)
    if size < 20:
      starberry.pencolor("green")
    else:
      starberry.pencolor("black")
      
  starberry.circle(size)

elif shape == "triangle":
  if size > 50:
    starberry.pensize(5)
    if size > 100:
      starberry.pencolor("purple")
    else:
      starberry.pencolor("orange")
  else:
    starberry.pensize(2)
    if size < 20:
      starberry.pencolor("pink")
    else:
      starberry.pencolor("brown")
  
  x = 0
  while x < 3:
    starberry.forward(size)
    starberry.right(120)
    x += 1

else:
  print("Invalid shape entered!")

turtle.done()