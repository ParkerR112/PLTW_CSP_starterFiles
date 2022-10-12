# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random

#-----game configuration----
style = ('Courier', 30, 'italic')
leaderboardStyle = ('Courier', 15)
score = 0
timer = 5
counterInterval = 1000
scores = []
FONT = ('Arial', 12, 'bold')

#-----initialize turtle-----
mole = turtle.Turtle(shape="square")
mole.penup()

scribe = turtle.Turtle()
scribe.hideturtle()

scorer = turtle.Turtle()
scorer.hideturtle()


counter = turtle.Turtle()
counter.hideturtle()

button = turtle.Turtle(shape='circle')
button.hideturtle()
button.speed(0)
button.fillcolor('red')

wn = turtle.Screen()

#-----game functions--------
def move(x, y, t):
  t.penup()
  t.goto(x, y)
  t.pendown()
  
def setup():
  scribe.speed(0)
  move(-160, 160, scribe)
  scribe.setheading(270)
  for i in range(4):
    scribe.forward(320)
    scribe.left(90)
    
  move(0, 200, scribe)
  scribe.write('Whack A Mole', font=style, align='center')

  button.hideturtle()
  button.speed(0)
  button.fillcolor('red')
  move(0, -225, button)
  button.penup()
  button.write("Restart", align='center', font=FONT)
  button.sety(-193)
  button.showturtle()
  
  move(125, -225, counter)

  move(-125, -225, scorer)


def countdown():
  global timer
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=FONT, align='center')
  else:
    counter.write(str(timer), font=style, align='center')
    timer -= 1
    counter.getscreen().ontimer(countdown, counterInterval) 

def scoring():
  global score
  score += 1
  scorer.clear()
  scorer.write(score, font=style, align='center')
  
def moleHit(x, y):
  global score, timer
  if timer > 0:
    scoring()
    if score > 0:
      timer = 5
    if score > 10:
      timer = 4
    if score > 20:
      timer = 3
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    mole.goto(x, y)

def restart(x, y):
  global score, timer

  if timer <= 0:
    counter.getscreen().ontimer(countdown, counterInterval) 
  score = 0
  timer = 5
  
  counter.clear()
  
  
  scorer.clear()
  scorer.write(score, font=style, align='center')
  
#-----events----------------
setup()

mole.onclick(moleHit)
button.onclick(restart)
wn.ontimer(countdown, counterInterval) 

wn.mainloop()