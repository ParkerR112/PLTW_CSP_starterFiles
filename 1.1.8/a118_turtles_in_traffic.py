#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["classic", "turtle", "circle", "square", "triangle"]
collision_shape = "arrow"
collision_color = "brown"
horiz_colors = ["red", "blue", "green", "orange", "purple"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo"]

tloc = 50
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

for step in range(50):
  turtles = vert_turtles + horiz_turtles
  for t in turtles:
    t.forward(10)

  for vt in vert_turtles:
    for ht in horiz_turtles:
      if abs(ht.xcor() - vt.xcor()) <= 10 and abs(ht.ycor() - vt.ycor()) <= 10:
        vt.shape(collision_shape)
        vt.color(collision_color)
        ht.shape(collision_shape)
        ht.color(collision_color)
        vert_turtles.remove(vt)
        horiz_turtles.remove(ht)

wn = trtl.Screen()
wn.mainloop()
