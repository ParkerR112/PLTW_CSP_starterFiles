#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
def move(x, y):
  spider.penup()
  spider.goto(x, y)
  spider.pendown()
def leg(x, y, headed):
  spider.penup()
  spider.goto(x, y)
  spider.setheading(headed)
  spider.pendown()
  spider.circle(150, 80)

# draw the body of the spider
spider = trtl.Turtle()
spider.shape("circle")
spider.pensize(5)
spider.begin_fill()
spider.circle(50)
spider.end_fill()

# draw the head of the spider
move(0, -55)
spider.shape("circle")
spider.pensize(5)
spider.begin_fill()
spider.circle(30)
spider.end_fill()

# draw the eyes of the spider
move(-10, -40)
spider.color("purple")
spider.stamp()
move(10, -40)
spider.stamp()

# Drawing Legs
spider.color("black")
leg(0, 50, 200)
leg(0, 50, 180)
leg(0, 50, 160)
leg(0, 50, 140)
leg(96.42, -117, 80)
leg(147.72, -73.95, 100)
leg(181.21, -15.95, 120)
leg(192.84, 50, 140)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
