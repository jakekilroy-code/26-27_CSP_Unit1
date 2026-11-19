

#a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----


spot_color = "lavender"
spot_size = 5
spot_shape = "circle"

score = 0

font_setup = ("Arial", 20, "normal")
spot = trtl.Turtle()

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

colors = ["red", "orange", "yellow", "green", "blue", "violet"]



spot.shapesize(spot_size)
#-----initialize turtle-----

spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.color(spot_color)


score_writer = trtl.Turtle()
score_writer.shapesize(1)
score_writer.color("Green")
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(370,300)

counter = trtl.Turtle()
counter.color("red")
counter.penup()
counter.hideturtle()
#-----game functions--------
def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        change_postition()
        update_score()
    else:
        spot.hideturtle()
def countdown():
  global timer, timer_up
  counter.clear()
  counter.goto(-200, 200)
  counter.write("Timer: " + str(timer), font=font_setup)
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def change_postition():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)
    spot.goto(new_xpos, new_ypos)

def update_score():
    global score
    print("Score " + str(score))
    score += 1
    score_writer.clear()
    score_writer.write(score, font = font_setup)
spot.penup()

def changing_color():
    global spot_color
    spot_color = rand.choice(colors)
    spot.stamp()
    spot.color(rand.choice(colors))


changing_color()
#-----events----------------
spot.onclick(spot_clicked)



wn = trtl.Screen()
wn.bgcolor("peachpuff")
wn.ontimer(countdown, counter_interval)
wn.mainloop()