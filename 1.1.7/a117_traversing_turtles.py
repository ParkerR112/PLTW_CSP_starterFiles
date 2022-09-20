#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)

#  set the starting x and y
startx = 0
starty = 0
startheading = 0
# create the loop to draw the shape
for t in my_turtles:
  index = my_turtles.index(t)
  t.color(turtle_colors[index])
  t.goto(startx, starty)
  t.setheading(startheading)
  t.pendown()
  t.right(70)     
  t.forward(70)

#	increment the startx and starty variables
  startx = t.xcor()
  starty = t.ycor()
  startheading = t.heading()

wn = trtl.Screen()
wn.mainloop()
