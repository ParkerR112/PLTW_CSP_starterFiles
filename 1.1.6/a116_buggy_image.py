#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

# draw the body of the spider
spider = trtl.Turtle()
spider.shape("circle")
spider.pensize(40)
spider.circle(20)


# configure spider legs
numOfLegs = 8
legLength = 70
degreeOfTurn = 270 / numOfLegs
spider.color("black")
spider.pensize(5)
interator = 0

# draw the legs of the spider
while (interator < numOfLegs):
  spider.goto(0,20)
  spider.setheading((degreeOfTurn*interator) - 27)
  spider.forward(legLength)
  interator += 1

# draw the eyes of the spider
spider.penup()
spider.pensize(5)
spider.goto(-15, 10)
spider.pendown()
spider.color("white")
spider.stamp()
spider.penup()
spider.goto(15, 10)
spider.pendown()
spider.stamp()

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
