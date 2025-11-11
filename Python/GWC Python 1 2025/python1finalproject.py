# Hachiware Drawing (from Chiikawa)!
import turtle
import random

# background
s = turtle.Screen()
s.bgcolor("white")
s.setup(400, 400)

turtle.colormode(255)

red = random.randint(1, 255)
green = random.randint(1, 255)
blue = random.randint(1, 255)
rgb = [red, green, blue]

bg = turtle.Turtle()
bg.speed(0)
bg.penup()
bg.goto(-250, -100)

while True:
  bg.fillcolor(rgb)
  bg.color(rgb)
  bg.pendown()
  break

bg.begin_fill()
for _ in range(2):
  bg.forward(500)
  bg.right(90)
  bg.forward(250)
  bg.right(90)
bg.end_fill()

# color variables
outline = "#35120D"
mainColor = "white"
secondColor = "#7CADC5"
blush = "#E8B2B9"

# head turtle
head = turtle.Turtle()
head.hideturtle()
head.color(outline)
head.speed(0)
head.pensize(3)

# face turtle
face = turtle.Turtle()
face.hideturtle()
face.color(outline)
face.speed(0)
face.pensize(5)

# body turtle
body = turtle.Turtle()
body.hideturtle()
body.color(outline)
body.speed(0)
body.pensize(3)

'''---------------------------------------------'''

# head features
head.showturtle()

# base head
def draw_head(r):
  head.penup()
  head.goto(-75, 0)
  head.pendown()
  head.fillcolor(mainColor)
  head.begin_fill()
  
  head.right(45)
  for _ in range(2):
    head.circle(r, 90)
    head.circle(r / 2, 90)
  head.end_fill()

# left ear
def draw_leftEar(ear):
  head.penup()
  head.goto(-55, 85)
  head.setheading(0)
  head.pendown()
  head.fillcolor(secondColor)
  head.begin_fill()
  
  head.forward(15)
  head.left(110)
  
  head.forward(ear)
  head.left(140)
  
  head.forward(ear + 5)
  head.end_fill()

# right ear
def draw_rightEar(ear):
  head.penup()
  head.goto(45, 85)
  head.setheading(180)
  head.pendown()
  head.fillcolor(secondColor)
  head.begin_fill()
  
  head.forward(15)
  head.right(110)
  
  head.forward(ear)
  head.right(140)
  
  head.forward(ear + 5)
  head.end_fill()

# forehead features
def draw_4head(x):
  head.penup()
  head.goto(0, 100)
  head.setheading(-90)
  head.pendown()
  head.fillcolor(secondColor)
  
  head.begin_fill()
  for _ in range(50):
    head.forward(x)
    head.right(3)
  head.end_fill()
  
  head.setheading(45)
  
  head.begin_fill()
  for _ in range(45):
    head.forward(x)
    head.right(1.35)
  head.end_fill()
  
  head.begin_fill()
  for _ in range(30):
    head.forward(x)
    head.right(0.95)
  head.end_fill()
  
  head.setheading(225)
  
  head.begin_fill()
  for _ in range(48):
    head.forward(x)
    head.right(3)
  head.end_fill()
  
  head.setheading(0)
  head.forward(5)
  head.setheading(-27)
  head.forward(6)
  head.color(secondColor)
  head.pensize(5)
  head.forward(44)

# initiating head functions
draw_head(100)
draw_leftEar(30)
draw_rightEar(30)
draw_4head(1.75)

head.hideturtle()

'''---------------------------------------------'''

# face features
face.showturtle()

# eyebrows
def draw_eyebrows(x):
  face.penup()
  face.goto(-29, 60)
  face.pendown()
  
  face.forward(x)
  
  face.penup()
  face.goto(18, 60)
  face.pendown()
  
  face.forward(x)

# eyes
def draw_eyes(r):
  face.penup()
  face.goto(-29, 35)
  face.pendown()
  face.fillcolor(outline)
  
  face.begin_fill()
  face.circle(r)
  face.end_fill()
  
  face.penup()
  face.goto(21, 35)
  face.pendown()
  
  face.begin_fill()
  face.circle(r)
  face.end_fill()

# eye highlights
def draw_eyeHighlights(r):
  face.pensize(1)
  face.penup()
  face.goto(-31, 44)
  face.pendown()
  
  face.color(mainColor)
  face.fillcolor(mainColor)
  
  face.begin_fill()
  face.right(45)
  for _ in range(2):
    face.circle(r, 90)
    face.circle(r / 2, 90)
  face.end_fill()
  
  face.penup()
  face.goto(23, 46)
  face.pendown()
  face.setheading(-205)
  
  face.begin_fill()
  face.right(45)
  for _ in range(2):
    face.circle(r, 90)
    face.circle(r / 2, 90)
  face.end_fill()
  
  face.penup()
  face.pensize(4)
  face.goto(-31, 39)
  face.pendown()
  face.setheading(-45)
  
  for _ in range(5):
    face.forward(1)
    face.left(25)
  
  face.penup()
  face.pensize(4)
  face.goto(18, 39)
  face.pendown()
  face.setheading(-45)
  
  for _ in range(5):
    face.forward(1)
    face.left(25)

# blush
def draw_blush(r):
  face.penup()
  face.goto(-60, 23)
  face.pendown()
  
  face.setheading(0)
  face.color(blush)
  face.fillcolor(blush)
  
  face.begin_fill()
  face.right(45)
  for _ in range(2):
    face.circle(r, 90)
    face.circle(r / 2, 90)
  face.end_fill()
  
  face.penup()
  face.goto(35, 23)
  face.pendown()
  
  face.setheading(0)
  face.color(blush)
  face.fillcolor(blush)
  
  face.begin_fill()
  face.right(45)
  for _ in range(2):
    face.circle(r, 90)
    face.circle(r / 2, 90)
  face.end_fill()

# the lines in the blush
def draw_blushLines():
  x1 = -58
  y1 = 32
  
  face.penup()
  face.goto(x1, y1)
  face.pendown()
  
  face.setheading(240)
  face.pensize(3)
  face.color(outline)
  
  for _ in range(4):
    face.forward(random.randint(3, 7))
    x1 += 4.5
    
    face.penup()
    face.goto(x1, y1)
    face.pendown()
  
  x2 = 37
  y2 = 32
  
  face.penup()
  face.goto(x2, y2)
  face.pendown()
  
  for _ in range(4):
    face.forward(random.randint(3, 7))
    x2 += 4.5
    
    face.penup()
    face.goto(x2, y2)
    face.pendown()

# nose and mouth
def draw_noseMouth(a):
  face.penup()
  face.goto(-2.5, 26.5)
  face.pendown()
  
  face.setheading(120)
  face.pensize(5)
  
  for _ in range(3):
    face.forward(a)
    face.right(120)
    
  face.setheading(-90)
  face.pensize(3)
  
  for _ in range(9):
    face.forward(2)
    face.right(20)
  
  face.penup()
  face.goto(-2.5, 26.5)
  face.pendown()
  face.setheading(-90)
  
  for _ in range(9):
    face.forward(2)
    face.left(20)
  
  face.penup()
  face.goto(-5, 15)
  face.pendown()
  
  face.setheading(-20)
  
  for _ in range(5):
    face.forward(1)
    face.left(10)

# initiating face functions
draw_eyebrows(3)
draw_eyes(7.5)
draw_eyeHighlights(4)
draw_blush(12.5)
draw_blushLines()
draw_noseMouth(2.5)
  
face.hideturtle()

'''---------------------------------------------'''

# body
body.showturtle()

# torso
def draw_torso():
  body.penup()
  body.goto(-60, -10)
  body.pendown()
  
  body.setheading(-90)
  body.fillcolor(mainColor)
  
  body.begin_fill()
  body.forward(60)
  body.left(90)
  
  body.setheading(-20)
  
  for _ in range(25):
    body.forward(4.45)
    body.left(1.6)
  
  body.setheading(90)
  
  body.begin_fill()
  body.forward(60)
  body.left(90)
  body.end_fill()
  
  body.color(mainColor)
  body.forward(110)
  
# arms
def draw_arms(a, b):
  # left arm
  body.penup()
  body.goto(-67, -7.5)
  body.pendown()
  
  body.setheading(-90)
  body.color(outline)
  body.fillcolor(mainColor)
  
  body.begin_fill()
  body.forward(a)
  
  for _ in range(5):
    body.forward(b)
    body.left(30)
  
  body.setheading(90)
  
  body.forward(a)
  body.end_fill()
  
  # right arm  
  body.penup()
  body.goto(57, -7.5)
  body.pendown()
  
  body.setheading(-90)
  
  body.begin_fill()
  body.forward(a)
  
  for _ in range(5):
    body.forward(b)
    body.right(30)
  
  body.setheading(90)
  
  body.forward(a)
  body.end_fill()

# legs
def draw_legs(a, b):
  # left leg
  body.penup()
  body.goto(-60, -70)
  body.pendown()
  
  body.setheading(-90)
  
  body.begin_fill()
  body.forward(a)
  
  for _ in range(5):
    body.forward(b)
    body.left(30)
  
  body.setheading(90)
  
  body.forward(a)
  body.end_fill()
  
  # right leg  
  body.penup()
  body.goto(50, -70)
  body.pendown()
  
  body.setheading(-90)
  
  body.begin_fill()
  body.forward(a)
  
  for _ in range(5):
    body.forward(b)
    body.right(30)
  
  body.setheading(90)
  
  body.forward(a)
  body.end_fill()
  
  body.penup()
  body.goto(-55, -65)
  body.pendown()
  
  body.color(mainColor)
  body.pensize(7)
  body.setheading(-90)
  
  body.forward(20)
  
  body.penup()
  body.goto(45, -65)
  body.pendown()
  
  body.forward(20)

# initiating body functions
draw_torso()
draw_arms(18, 2.5)
draw_legs(13, 2.5)

turtle.done()