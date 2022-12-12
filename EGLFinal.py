
import matplotlib.pyplot as plt
import math
from turtle import *


# Declaring all variables in global
line_len = None
d_hp = None
d_vp = None

hp_angle = None
vp_angle = None

fv_coord1 = None
fv_x_coord1 = None
fv_y_coord1 = None

tv_coord1 = None
tv_x_coord1 = None
tv_y_coord1 = None

fv_coord2 = None
fv_x_coord2 = None
fv_y_coord2 = None

tv_coord2 = None
tv_x_coord2 = None
tv_y_coord2 = None

fv_coord3 = None
fv_x_coord3 = None
fv_y_coord3 = None

tv_coord3 = None
tv_x_coord3 = None
tv_y_coord3 = None

fv_coord4 = None
fv_x_coord4 = None
fv_y_coord4 = None

tv_coord4 = None
tv_x_coord4 = None
tv_y_coord4 = None

fv_angle4 = None
tv_angle4 = None

fv_len4 = None
tv_len4 = None

fv_p_len4 = None
fv_h_len4 = None
fv_b_len4 = None

tv_p_len4 = None
tv_h_len4 = None
tv_b_len4 = None

fv_d_end_hp = None
tv_d_end_hp = None


def default_input():

    global line_len, d_hp, d_vp, fv_coord1, fv_x_coord1, fv_y_coord1, tv_coord1, tv_x_coord1, tv_y_coord1

    # distance from hp, vp
    d_hp = int(input("Distance from HP: "))
    d_vp = int(input("Distance from VP: "))

    # fv, tv  coordinates of starting point

    fv_coord1 = (0, d_hp)
    fv_x_coord1, fv_y_coord1 = fv_coord1

    tv_coord1 = (0, -1*d_vp)
    tv_x_coord1, tv_y_coord1 = tv_coord1

    line_len = int(input("Length of line: "))


def calculateEverything():

    # declaring all variables of function in global
    global fv_coord1, fv_x_coord1, fv_y_coord1, tv_coord1, tv_x_coord1, tv_y_coord1
    global fv_coord2, fv_x_coord2, fv_y_coord2, tv_coord2, tv_x_coord2, tv_y_coord2
    global fv_coord3, fv_x_coord3, fv_y_coord3, tv_coord3, tv_x_coord3, tv_y_coord3
    global fv_coord4, fv_x_coord4, fv_y_coord4, tv_coord4, tv_x_coord4, tv_y_coord4
    global fv_p_len2, fv_b_len2, tv_p_len2, tv_b_len2
    global fv_p_len4, fv_h_len4, fv_b_len4, tv_p_len4, tv_h_len4, tv_b_len4
    global fv_angle4, tv_angle4

    fv_p_len2 = math.sin(math.radians(hp_angle)) * line_len
    fv_b_len2 = math.cos(math.radians(hp_angle)) * line_len

    tv_p_len2 = math.sin(math.radians(vp_angle)) * line_len
    tv_b_len2 = math.cos(math.radians(vp_angle)) * line_len

    if fv_y_coord1 < 0 and fv_p_len2 > 0:
        fv_p_len2 *= -1
    if tv_y_coord1 < 0 and tv_p_len2 > 0:
        tv_p_len2 *= -1

    fv_coord2 = (fv_x_coord1+fv_b_len2, fv_y_coord1+fv_p_len2)
    fv_x_coord2, fv_y_coord2 = fv_coord2

    tv_coord2 = (tv_x_coord1+tv_b_len2, tv_y_coord1+tv_p_len2)
    tv_x_coord2, tv_y_coord2 = tv_coord2

    fv_coord3 = (fv_x_coord1+tv_b_len2, fv_y_coord1)
    fv_x_coord3, fv_y_coord3 = fv_coord3

    tv_coord3 = (tv_x_coord1+fv_b_len2, tv_y_coord1)
    tv_x_coord3, tv_y_coord3 = tv_coord3

    fv_h_len4 = math.dist([fv_x_coord1], [tv_x_coord2])
    fv_p_len4 = math.dist([fv_y_coord1], [fv_y_coord2])
    fv_angle4 = math.degrees(math.asin(fv_p_len4/fv_h_len4))
    fv_b_len4 = math.cos(math.radians(fv_angle4)) * fv_h_len4

    tv_h_len4 = math.dist([tv_x_coord1], [fv_x_coord2])
    tv_p_len4 = math.dist([tv_y_coord1], [tv_y_coord2])
    tv_angle4 = math.degrees(math.asin(tv_p_len4/tv_h_len4))
    tv_b_len4 = math.cos(math.radians(tv_angle4)) * tv_h_len4

    if fv_y_coord1 < 0 and fv_p_len4 > 0:
        fv_p_len4 *= -1
    if tv_y_coord1 < 0 and tv_p_len4 > 0:
        tv_p_len4 *= -1

    fv_coord4 = (fv_x_coord1+fv_b_len4, fv_y_coord1+fv_p_len4)
    tv_coord4 = (tv_x_coord1+tv_b_len4, tv_y_coord1+tv_p_len4)

    fv_x_coord4, fv_y_coord4 = fv_coord4
    tv_x_coord4, tv_y_coord4 = tv_coord4


def q1input():
    global hp_angle, vp_angle
    hp_angle = int(input("Inclination to HP: "))
    vp_angle = int(input("Inclination to VP: "))


def q1calculation():
    pass


def q2input():
    global fv_d_end_hp, tv_d_end_hp
    fv_d_end_hp = int(input('Enter distance of end point from HP'))
    tv_d_end_hp = int(input('Enter distance of end point from VP'))


def q2calculation():
    global fv_p_len2, tv_p_len2, hp_angle, vp_angle

    fv_p_len2 = fv_d_end_hp - d_hp
    tv_p_len2 = tv_d_end_hp - d_vp
    hp_angle = math.degrees(math.asin(fv_p_len2/line_len))
    vp_angle = math.degrees(math.asin(tv_p_len2/line_len))


def q3input():
    global hp_angle, tv_angle4
    hp_angle = int(input("Inclination to HP: "))
    tv_angle4 = int(input("Angle of TV to XY line: "))


def q3calculation():
    global fv_p_len2, tv_angle4, fv_b_len2,  tv_b_len4,  tv_h_len4,  tv_p_len4, fv_x_coord2, fv_y_coord2, vp_angle
    fv_p_len2 = math.sin(math.radians(hp_angle)) * line_len
    fv_b_len2 = math.cos(math.radians(hp_angle)) * line_len

    fv_coord2 = (fv_x_coord1+fv_b_len2, fv_y_coord1+fv_p_len2)
    fv_x_coord2, fv_y_coord2 = fv_coord2

    tv_h_len4 = math.dist([fv_x_coord1], [fv_x_coord2])
    tv_p_len4 = math.sin(math.radians(tv_angle4))*tv_h_len4
    tv_b_len4 = math.cos(math.radians(tv_angle4))*tv_h_len4

    vp_angle = math.degrees(math.asin(tv_p_len4/line_len))


def q4input():
    global fv_len4, tv_len4
    fv_len4 = int(input("Length of FV: "))
    tv_len4 = int(input("Length of TV: "))


def q4calculation():
    global fv_b_len2, tv_b_len2, hp_angle, vp_angle
    fv_b_len2 = tv_len4
    tv_b_len2 = fv_len4

    hp_angle = math.degrees(math.acos(fv_b_len2/line_len))
    vp_angle = math.degrees(math.acos(tv_b_len2/line_len))


def matplotlib_plot():

    plt.grid(True)

    x = [fv_x_coord1, fv_x_coord4]
    y = [fv_y_coord1, fv_y_coord4]

    plt.plot(x, y, label="front view1")

    x = [fv_x_coord1, fv_x_coord2]
    y = [fv_y_coord1, fv_y_coord2]

    plt.plot(x, y, label="front view2")

    x = [tv_x_coord1, tv_x_coord4]
    y = [tv_y_coord1, tv_y_coord4]

    plt.plot(x, y, label="top view1")

    x = [tv_x_coord1, tv_x_coord2]
    y = [tv_y_coord1, tv_y_coord2]

    plt.plot(x, y, label="top view2")

    # horizontal line

    plt.plot([0, 200], [0, 0], label="horizontal line")

    plt.xlim(-200, 200)
    plt.ylim(-100, 100)

    plt.show()


def draw_projection():

    # Import and initialize turtle
    screensize(canvheight=100, canvwidth=100)

    # Draw the true lines

    hideturtle()
    clear()

    # Horizontal line
    goto((-10, 0))
    pendown()
    pensize(3)
    goto((100, 0))

    # Go to front view coord 1
    penup()
    goto(fv_coord1)

    # Draw till front view coord 2
    pendown()
    pensize(3)
    goto(fv_coord2)

    # Go to top view coord 1
    penup()
    goto(tv_coord1)

    # Draw till top view coord 2
    pendown()
    pensize(3)
    goto(tv_coord2)

    # Draw horizontal line at fv_y_coord1
    penup()
    goto((0, fv_y_coord1))
    pendown()
    pensize(1)
    goto((100, fv_y_coord1))

    # Draw horizontal line at fv_y_coord2
    penup()
    goto((0, fv_y_coord2))
    pendown()
    pensize(1)
    goto(100, fv_y_coord2)

    # Draw horizontal line at tv_y_coord1
    penup()
    goto((0, tv_y_coord1))
    pendown()
    goto((100, tv_y_coord1))

    # Draw horizontal line at tv_y_coord2
    penup()
    goto(0, tv_y_coord2)
    pendown()
    goto((100, tv_y_coord2))

    # Draw projections from fv to tv
    penup()
    goto(fv_coord2)
    pendown()
    goto(tv_coord3)

    # Draw projections from tv to fv
    penup()
    goto(tv_coord2)
    pendown()
    goto(fv_coord3)

    # Draw arc in fv
    penup()
    goto(fv_coord3)
    setheading(90)
    pendown()
    circle(fv_h_len4, fv_angle4)

    # Get the coordinates fv of projection
    fv_final_coord = pos()

    # Draw arc in tv
    penup()
    goto(tv_coord3)
    setheading(270)
    pendown()
    circle(-tv_h_len4, tv_angle4)

    # Get the coordinates tv of projection
    tv_final_coord = pos()

    # Draw final projection
    penup()
    goto(fv_coord1)
    pensize(3)
    pendown()
    goto(fv_final_coord)
    penup()
    goto(tv_coord1)
    pensize(3)
    pendown()
    goto(tv_final_coord)

    # Add labels horizontal line
    penup()
    goto((-10, 0))
    write("X", align="left", font=("Arial", 10, "italic"))
    goto((100, 0))
    write("Y", align="right", font=("Arial", 10, "italic"))

    # Add labels FV

    goto(fv_coord1)
    write("A`", align="left", font=("Arial", 10, "normal"))
    goto(fv_coord2)
    write("B2`", align="left", font=("Arial", 10, "normal"))
    goto(fv_coord3)
    write("B1`", align="left", font=("Arial", 10, "normal"))
    goto(fv_coord4)
    write("B`", align="left", font=("Arial", 10, "normal"))

    # Add labels TV
    goto(tv_coord1)
    write("A", align="left", font=("Arial", 10, "normal"))
    goto(tv_coord2)
    write("B2", align="left", font=("Arial", 10, "normal"))
    goto(tv_coord3)
    write("B1", align="left", font=("Arial", 10, "normal"))
    goto(tv_coord4)
    write("B", align="left", font=("Arial", 10, "normal"))

    # Write metadata
    goto((150, 150))
    write("Θ = " + str(round(hp_angle)) + "°",
          align="left", font=("Arial", 10, "normal"))
    goto((150, 135))
    write("Φ = " + str(round(vp_angle)) + "°",
          align="left", font=("Arial", 10, "normal"))
    goto((150, 120))
    write("α = " + str(round(fv_angle4)) + "°",
          align="left", font=("Arial", 10, "normal"))
    goto((150, 105))
    write("β = " + str(round(tv_angle4)) + "°",
          align="left", font=("Arial", 10, "normal"))
    goto((150, 90))
    write("True length =" + str(round(line_len)) + "mm",
          align="left", font=("Arial", 10, "normal"))
    goto((150, 75))
    write("FV length =" + str(round(fv_h_len4)) + "mm",
          align="left", font=("Arial", 10, "normal"))
    goto((150, 60))
    write("TV length =" + str(round(tv_h_len4)) + "mm",
          align="left", font=("Arial", 10, "normal"))
    
    print("Drawn, check the new window for the solution.")

    exitonclick()


user_input = int(input("""
Please choose between the following options:
1) Input distance to HP, distance to VP, length of line, inclination to HP, inclination to VP, 
2) Input distance to HP, distance to VP, length of line, distance of end point to HP, distance of end point to VP
3) Input distance to HP, distance to VP, length of line, inclination to HP, angle of TV projection to XY line
4) Input distance to HP, distance to VP, length of line, length of FV projection, length of TV projection
"""))
if user_input not in [1, 2, 3, 4]:
    raise ValueError("Please enter a valid option")

if user_input == 1:
    default_input()
    q1input()
    q1calculation()
    calculateEverything()
    draw_projection()

if user_input == 2:
    default_input()
    q2input()
    q2calculation()
    calculateEverything()
    draw_projection()

if user_input == 3:
    default_input()
    q3input()
    q3calculation()
    calculateEverything()
    draw_projection()

if user_input == 4:
    default_input()
    q4input()
    q4calculation()
    calculateEverything()
    draw_projection()
