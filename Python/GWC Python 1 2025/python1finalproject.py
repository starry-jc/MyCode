# Hachiware Drawing (from Chiikawa)!
# importing modules
import turtle
import random

# creating screen for background
s = turtle.Screen()
s.bgcolor("white")  # main bg color = white
s.setup(400, 400)

turtle.colormode(255)

# setting up random rgb values for bg second color
red = random.randint(1, 255)
green = random.randint(1, 255)
blue = random.randint(1, 255)
rgb = [red, green, blue]

# creating bg second color as a turtle
bg = turtle.Turtle()
bg.speed(0)
bg.penup()
bg.goto(-250, -100) # moving it to the ground

# conditional that will always run the bg second color
while True:
  bg.color(rgb)
  bg.pendown()

  bg.begin_fill()
  for _ in range(2):
    bg.forward(500)
    bg.right(90)
    bg.forward(250)
    bg.right(90)
  bg.end_fill()
  
  break

# color variables
outline = "#35120D"
mainColor = "white"
secondColor = "#7CADC5"
blush = "#E8B2B9"

'''---------------------------------------------'''

# creating turtles
# head turtle
head = turtle.Turtle()
head.hideturtle() # hiding these (for now) so they don't mess with the drawing
head.color(outline) # defaulting the stroke outlines to be the outline color
head.speed(0) # full speed ahead!
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

# starting with the head
head.showturtle() # showtime!

# base head function
def draw_head(r): # r = radius for ovals
  # creating the oval
  head.penup()
  head.goto(-75, 0)
  head.pendown()
  
  head.fillcolor(mainColor)
  
  # random nested loop for the requirement
  while True:
    head.begin_fill()
    head.right(45)
    for _ in range(2):
      head.circle(r, 90)
      head.circle(r/2, 90)
    head.end_fill()
    
    break

# left ear function
def draw_leftEar(ear):  # ear = left ear size
  head.penup()
  head.goto(-55, 85)
  head.pendown()
  
  head.setheading(0)
  head.fillcolor(secondColor)
  
  head.begin_fill()
  head.forward(15)
  head.left(110)
  
  head.forward(ear)
  head.left(140)
  
  head.forward(ear + 5)
  head.end_fill()

# right ear function
def draw_rightEar(ear): # ear = right ear size
  head.penup()
  head.goto(45, 85)
  head.pendown()
  
  head.setheading(180)
  head.fillcolor(secondColor)
  
  head.begin_fill()
  head.forward(15)
  head.right(110)
  
  head.forward(ear)
  head.right(140)
  
  head.forward(ear + 5)
  head.end_fill()

# forehead function
def draw_4head(fore):  # fore = forehead size factor
  x = 0
  y = 0
  # left curvy half
  head.penup()
  head.goto(0, 100)
  head.pendown()
  
  head.setheading(-90)
  head.fillcolor(secondColor)
  
  head.begin_fill()
  while x < 50:
    head.forward(fore)
    head.right(3)
    
    x += 1
  head.end_fill()
  
  # tracing and filling top LEFT part of oval
  head.setheading(45)
  
  head.begin_fill()
  for _ in range(45):
    head.forward(fore)
    head.right(1.35)
  head.end_fill()
  
  # tracing and filling top RIGHT part of oval
  head.begin_fill()
  while y < 30:
    head.forward(fore)
    head.right(0.95)
    
    y += 1
  head.end_fill()
  
  # right curvy half
  head.setheading(225)
  
  head.begin_fill()
  for _ in range(48):
    head.forward(fore)
    head.right(3)
  head.end_fill()
  
  # filling in gaps
  head.setheading(0)
  head.forward(5)
  head.setheading(-27)
  head.forward(6)
  head.color(secondColor)
  head.pensize(5)
  head.forward(44)

# calling all head functions!
draw_head(100)
draw_leftEar(30)
draw_rightEar(30)
draw_4head(1.75)

# done with the head!
head.hideturtle()

'''---------------------------------------------'''

# next is the face
face.showturtle()

# eyebrows function
def draw_eyebrows(brow):  # brow = brow length
  face.penup()
  face.goto(-29, 60)
  face.pendown()
  
  face.forward(brow)
  
  face.penup()
  face.goto(18, 60)
  face.pendown()
  
  face.forward(brow)

# eyes
def draw_eyes(r): # r = eye radius
  # drawing left eye
  face.penup()
  face.goto(-29, 35)
  face.pendown()
  
  face.fillcolor(outline)
  
  face.begin_fill()
  face.circle(r)
  face.end_fill()
  
  # drawing right eye
  
  face.penup()
  face.goto(21, 35)
  face.pendown()
  
  face.begin_fill()
  face.circle(r)
  face.end_fill()

# eye highlights function
def draw_eyeHighlights(r):  # r = radius of top highlight
  z = 0
  a = 0
  # top left highlight
  face.penup()
  face.goto(-31, 44)
  face.pendown()
  
  face.pensize(1)
  face.color(mainColor)
  face.fillcolor(mainColor)
  
  face.begin_fill()
  face.right(45)
  while z < 2:
    face.circle(r, 90)
    face.circle(r / 2, 90)
    
    z += 1
  face.end_fill()
  
  # top right highlight
  
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
  
  # bottom left highlight
  
  face.penup()
  face.pensize(4)
  face.goto(-31, 39)
  face.pendown()
  face.setheading(-45)
  
  while a < 5:
    face.forward(1)
    face.left(25)
    
    a += 1
  
  # bottom right highlight
  
  face.penup()
  face.pensize(4)
  face.goto(18, 39)
  face.pendown()
  face.setheading(-45)
  
  for _ in range(5):
    face.forward(1)
    face.left(25)

# blush function
def draw_blush(r):  # r = radius for ovals
  b = 0
  # left base blush (light red oval)
  face.penup()
  face.goto(-60, 23)
  face.pendown()
  
  face.setheading(0)
  face.color(blush)
  face.fillcolor(blush)
  
  face.begin_fill()
  face.right(45)
  while b < 2:
    face.circle(r, 90)
    face.circle(r / 2, 90)
    
    b += 1
  face.end_fill()
  
  # right base blush (light red oval)
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

# the lines in the blush function
def draw_blushLines():
  c = 0
  # left side blush lines
  x1 = -58  # x coordinate 1 (left)
  y1 = 32 # y coordinate 1 (left)
  
  face.penup()
  face.goto(x1, y1)
  face.pendown()
  
  face.setheading(240)
  face.pensize(3)
  face.color(outline)
  
  while c < 4:
    face.forward(random.randint(3, 7))  # randomizing their sizes
    x1 += 4.5 # setting up the new x coordinate
    
    face.penup()
    face.goto(x1, y1) # moving the turtle to the next coordinates
    face.pendown()
    
    c += 1
  
  # right side blush lines)
  x2 = 37 # x coordinate 2 (right)
  y2 = 32 # y coordinate 2 (right)
  
  face.penup()
  face.goto(x2, y2)
  face.pendown()
  
  for _ in range(4):
    face.forward(random.randint(3, 7))
    x2 += 4.5
    
    face.penup()
    face.goto(x2, y2)
    face.pendown()

# nose and mouth function
def draw_noseMouth(nose): # nose = nose size
  d = 0
  e = 0
  # drawing the nose (tiny triangle)
  face.penup()
  face.goto(-2.5, 26.5)
  face.pendown()
  
  face.setheading(120)
  face.pensize(5)
  
  while d < 3:
    face.forward(nose)
    face.right(120)
    
    d += 1
    
  # left side of mouth
  face.setheading(-90)
  face.pensize(3)
  
  for _ in range(9):
    face.forward(2)
    face.right(20)
  
  # right side of mouth
  face.penup()
  face.goto(-2.5, 26.5)
  face.pendown()
  face.setheading(-90)
  
  while e < 9:
    face.forward(2)
    face.left(20)
    
    e += 1
  
  # chin
  face.penup()
  face.goto(-5, 15)
  face.pendown()
  
  face.setheading(-20)
  
  for _ in range(5):
    face.forward(1)
    face.left(10)

# calling all face functions!
draw_eyebrows(3)
draw_eyes(7.5)
draw_eyeHighlights(4)
draw_blush(12.5)
draw_blushLines()
draw_noseMouth(2.5)

# done with the face!
face.hideturtle()

'''---------------------------------------------'''

# body features
body.showturtle()

# torso function
def draw_torso():
  f = 0
  # left line torso
  body.penup()
  body.goto(-60, -10)
  body.pendown()
  
  body.setheading(-90)
  body.fillcolor(mainColor)
  
  body.begin_fill()
  body.forward(60)
  body.left(90)
  
  # bottom line torso (it's a slight curve)
  body.setheading(-20)
  
  while f < 25:
    body.forward(4.45)
    body.left(1.6)
    
    f += 1
  
  # right line torso
  body.setheading(90)
  
  body.begin_fill()
  body.forward(60)
  body.left(90)
  body.end_fill()
  
  # white top line torso
  body.color(mainColor)
  body.forward(110)
  
# arms function
def draw_arms(arm, r):  # arm = arm length; r = radius for curve
  g = 0
  # left arm
  body.penup()
  body.goto(-67, -7.5)  # omg 67 guys
  body.pendown()
  
  body.setheading(-90)
  body.color(outline)
  body.fillcolor(mainColor)
  
  body.begin_fill()
  body.forward(arm) # forward slight amount...
  
  # then curve!
  for _ in range(5):
    body.forward(r)
    body.left(30)
  
  body.setheading(90) # change direction
  
  body.forward(arm) # straight again
  body.end_fill()
  
  # right arm  
  body.penup()
  body.goto(57, -7.5)
  body.pendown()
  
  body.setheading(-90)
  
  body.begin_fill()
  body.forward(arm)
  
  while g < 5:
    body.forward(r)
    body.right(30)
    
    g += 1
  
  body.setheading(90)
  
  body.forward(arm)
  body.end_fill()

# legs
def draw_legs(leg, r):  # leg = leg length; r = radius of curve
  h = 0
  # left leg
  body.penup()
  body.goto(-60, -70)
  body.pendown()
  
  body.setheading(-90)
  
  body.begin_fill()
  body.forward(leg) # basically same thing as arm but shorter
  
  for _ in range(5):
    body.forward(r)
    body.left(30)
  
  body.setheading(90)
  
  body.forward(leg)
  body.end_fill()
  
  # right leg  
  body.penup()
  body.goto(50, -70)
  body.pendown()
  
  body.setheading(-90)
  
  body.begin_fill()
  body.forward(leg)
  
  while h < 5:
    body.forward(r)
    body.right(30)
    
    h += 1
  
  body.setheading(90)
  
  body.forward(leg)
  body.end_fill()
  
  # clean up on aisle left leg (hide part of an outline)
  body.penup()
  body.goto(-55, -65)
  body.pendown()
  
  body.color(mainColor)
  body.pensize(7) # trick is to make the turtle stroke big enough
  body.setheading(-90)
  
  body.forward(20)
  
  # clean up on aisle right leg (hide part of an outline)
  body.penup()
  body.goto(45, -65)
  body.pendown()
  
  body.forward(20)

# calling all body functions!
draw_torso()
draw_arms(18, 2.5)
draw_legs(13, 2.5)

# done with body!
body.hideturtle()

'''---------------------------------------------'''

# misc

# writer turtle
writer = turtle.Turtle()
writer.speed(0)
writer.penup()

# title function
def write_title(text):
  writer.goto(-50, 175)
  writer.pendown()
  writer.color(outline)
  
  writer.write(text, align="center", font=("Times New Roman", 12, "bold"))
  writer.hideturtle()

# author function
def write_author(text):
  writer.showturtle()
  writer.penup()
  writer.goto(-50, 150)
  writer.pendown()
  writer.color(secondColor)
  
  writer.write(text, align="center", font=("Times New Roman", 10, "italic"))
  writer.hideturtle()

# your last conditional, with love <3
if True:
  write_title("Hachiware Drawing (from Chiikawa)!")
  write_author("by AJC ⸜(｡˃ ᵕ ˂ )⸝♡")
else:
  pass

turtle.done()

# REQUIREMENTS CHECK:
  # Colors: 4 (+ 1 if you count random color bg)
  # Bg Colors: 2 (white + random)
  # Conditionals: 2 (while loops + if statement)
  # Random Variables: 2 (bg color + blush lines)
  # Distinct Data Types: enough?
  # Nested Loops: 1 (while True: ... for _ in range(2):...)
  # Turtle Commands: too many
  # Use of Return Statements: sort of??
  # Use of a list: 1 (rgb)