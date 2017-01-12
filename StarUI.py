from turtle import *
import turtle

def angle(p_given):
    p = p_given
    if p % 2 == 0:
        if p / 2 % 2 == 0:
            a = 2 * 180 / p
        else:
            a = 4 * 180 / p
    else:
        a = 180 / p

def setup_screen():
    clearscreen()
    bgcolor("pink")
    pencolor("black")
    pensize(2)
    fillcolor("white")
    hideturtle()
    speed(10)
    setheading(0)

def draw_star(a):
    setup_screen()
    d = 400
    setx(- 0.5 * d)
    r = a + 180
    pendown()
    begin_fill()
    forward(d)
    right(r)
    x = 1
    while turtle.heading() != 0:
        forward(d)
        right(r)
        x = x + 1
    end_fill()

instructions = '''I will draw you a star. How many points do you want it to have?'''
screen = getscreen()
while True:
    p_given = screen.numinput('Drawing stars', instructions, 7, 3, 150)
    if p_given < 3:
        break
    else:
        a = angle(p_given)
        draw_star(a)

