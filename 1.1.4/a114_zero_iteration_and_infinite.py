#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

go = False
# Add a loop with a zero-iteration condition
while go == True:
    painter.circle(100)

# Add an infinite loop
while go == False:
    painter.circle(50)

wn = trtl.Screen()
wn.mainloop()
