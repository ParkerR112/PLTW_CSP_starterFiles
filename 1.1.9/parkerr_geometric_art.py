import turtle
import random
import math

wn = turtle.Screen()
t = turtle.Turtle()

def triangle(sideLength, x, y, fill):
    t.penup()
    a = sideLength / 2
    b = math.sqrt(sideLength**2 - a**2)
    finaly = y + b / 2
    t.goto(x, finaly)
    t.pendown()
    if fill == 0:
        t.begin_fill()
    t.right(random.randint(0, 360))
    for num in range(3):
        t.forward(sideLength)
        t.right(120)
    t.end_fill()

def square(sideLength, x, y, fill):
    t.penup()
    finalx = x - sideLength / 2
    finaly = y + sideLength / 2
    t.goto(finalx, finaly)
    t.pendown()
    if fill == 0:
        t.begin_fill()
    t.right(random.randint(0, 360))
    for num in range(4):
        t.forward(sideLength)
        t.right(90)
    t.end_fill()

def pentagon(sideLength, x, y, fill):
    t.penup()
    apothem = sideLength / (2 * (math.tan(36)))
    finaly = y + apothem
    t.goto(x, finaly)
    t.pendown()
    if fill == 0:
        t.begin_fill()
    t.right(random.randint(0, 360))
    for num in range(5):
        t.forward(sideLength)
        t.right(72)
    t.end_fill()

def hexagon(sideLength, x, y, fill):
    t.penup()
    apothem = sideLength / (2 * (math.tan(30)))
    finalx = x - sideLength / 2
    finaly = y + apothem
    t.goto(finalx, finaly)
    t.pendown()
    if fill == 0:
        t.begin_fill()
    t.right(random.randint(0, 360))
    for num in range(6):
        t.forward(sideLength)
        t.right(60)
    t.end_fill()

def octagon(sideLength, x, y, fill):
    t.penup()
    apothem = sideLength / (2 * (math.tan(22.5)))
    finalx = x - sideLength / 2
    finaly = y + apothem
    t.goto(finalx, finaly)
    t.pendown()
    if fill == 0:
        t.begin_fill()
    t.right(random.randint(0, 360))
    for num in range(8):
        t.forward(sideLength)
        t.right(45)
    t.end_fill()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
shapes = ['triangle', 'square', 'pentagon', 'hexagon', 'octagon']

t.pensize(8)

for i in range(10):
    shapeColor = random.choice(colors)
    shapeFill = random.randint(0, 1)

for i in colors:
    shape = random.choice(shapes)
    if shape == 'triangle':
        fill = random.randint(0, 1)
        t.fillcolor(i)
        t.pencolor(i)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        triangle(random.randint(100, 200), x, y, fill)
    if shape == 'square':
        fill = random.randint(0, 1)
        t.fillcolor(i)
        t.pencolor(i)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        square(random.randint(100, 200), x, y, fill)

wn.mainloop()