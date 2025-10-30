import turtle

turtle.colormode(255)

ted = turtle.Turtle()
i = 0

ted.fillcolor(81, 156, 93)

ted.begin_fill()

while i < 4:
  ted.forward(100)
  ted.right(90)
  i += 1

ted.end_fill()

turtle.done()