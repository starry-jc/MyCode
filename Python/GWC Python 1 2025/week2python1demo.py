import turtle

turtle.colormode(255)

mason = turtle.Turtle()

userColor = input("Choose a color: ")

mason.color(userColor)

angle = 60
length = 100

mason.forward(length)
mason.right(angle)
mason.forward(length)
mason.right(angle)
mason.forward(length)
mason.right(angle)
mason.forward(length)
mason.right(angle)
mason.forward(length)
mason.right(angle)
mason.forward(length)
mason.right(angle)

turtle.done()