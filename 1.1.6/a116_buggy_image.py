#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

# draw the body of the spider
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)

# configure spider legs
numOfLegs = 8
legLength = 70
degreeOfTurn = 360 / numOfLegs
spider.pensize(5)
interator = 0

# draw the legs of the spider
while (interator < numOfLegs):
  spider.goto(0,20)
  spider.setheading(degreeOfTurn*interator)
  spider.forward(legLength)
  interator += 1
  
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
