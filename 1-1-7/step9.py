# CODE TO COPY
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["magenta", "cyan", "pink", "brown", "green", "tan"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  t.color(turtle_colors.pop())
#
startx = 0
starty = 0
direction = 90
#
for t in my_turtles:
  t.penup()
  t.goto(startx, starty)
  t.setheading(direction)
  t.pendown()
  t.right(45)
  t.forward(50)
  direction = t.heading()
#
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()