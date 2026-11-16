# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "red"
spot_size = 5
spot_shape = "turtle"
score = 0



#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.turtlesize(spot_size)
spot.fillcolor(spot_color)

score_writer = trtl.Turtle()
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

#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()