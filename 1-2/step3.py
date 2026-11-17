# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "peachpuff"
spot_size = 10
spot_shape = "triangle"
score = 0



#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.turtlesize(spot_size)

spot.fillcolor(spot_color)
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.shapesize(3)
score_writer.color(spot_color)
score_writer.penup()
score_writer.goto(375, 320)

#-----game functions--------
def spot_clicked(x, y):
    change_position()
    update_score()
def change_position():
    new_xpos = rand.randint(-200, 200)
    new_ypos = rand.randint(-150, 150)

    spot.goto(new_xpos, new_ypos)
def update_score():
    global score
    print(score)
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)


spot.penup()

font_setup = ("arial", 20, "normal")
#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()