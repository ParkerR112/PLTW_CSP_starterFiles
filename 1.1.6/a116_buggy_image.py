#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
def move(x, y):
  spider.penup()
  spider.goto(x, y)
  spider.pendown()

# draw the body of the spider
spider = trtl.Turtle()
spider.shape("circle")
spider.pensize(40)
spider.circle(20)

# draw the head of the spider
move(0, -45)
spider.shape("circle")
spider.pensize(30)
spider.circle(10)

# configure spider legs
numOfLegs = 8
legLength = 70
degreeOfTurn = 270 / numOfLegs
spider.color("black")
spider.pensize(5)
interator = 0

# draw the legs of the spider
while (interator < numOfLegs):
  move(0,20)
  spider.setheading((degreeOfTurn*interator) - 27)
  spider.forward(legLength)
  interator += 1

# draw the eyes of the spider
spider.shapesize(1)
move(-10, -40)
spider.color("purple")
spider.stamp()
move(10, -40)
spider.stamp()

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
