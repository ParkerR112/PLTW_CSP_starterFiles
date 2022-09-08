#   a114_nested_loops_2.py 
import turtle as trtl

color1 = "orange"
color2 = "purple"

wn = trtl.Screen()
width = 400
height = 300

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

answer = "y"
while answer == "y":
  wn.clearscreen()
  painter.goto(0, 0)
  space = 1
  angle = int(input("angle:"))
  seg = int(360/angle)
  answer = input("again")
  