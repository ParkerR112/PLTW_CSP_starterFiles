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

colors = ['red', 'pink', 'orange', 'yellow', 'green', 'light green', 'blue', 'light blue', 'purple', 'magenta', 'dark blue', 'dark green']
shapes = ['triangle', 'square', 'pentagon', 'hexagon', 'octagon']

t.pensize(8)

for num in range(20):
    shape = random.choice(shapes)
    i = random.choice(colors)
    if shape == 'triangle':
        fill = random.randint(0, 1)
        t.fillcolor(i)
        t.pencolor(i)
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        triangle(random.randint(50, 90), x, y, fill)
    if shape == 'square':
        fill = random.randint(0, 1)
        t.fillcolor(i)
        t.pencolor(i)
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        square(random.randint(40, 80), x, y, fill)
    if shape == 'pentagon':
        fill =  random.randint(0, 1)
        t.fillcolor(i)
        t.pencolor(i)
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        pentagon(random.randint(30, 70), x, y, fill)
    if shape == 'hexagon':
        fill =  random.randint(0, 1)
        t.fillcolor(i)
        t.pencolor(i)
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        hexagon(random.randint(20, 60), x, y, fill)
    if shape == 'octagon':
        fill =  random.randint(0, 1)
        t.fillcolor(i)
        t.pencolor(i)
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        octagon(random.randint(10, 50), x, y, fill)
    
t.hideturtle()
wn.mainloop()
