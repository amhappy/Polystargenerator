from turtle import *
import turtle

# I seperately define the screen setup
def setup_screen():
    clearscreen()
    bgcolor("pink")
    pencolor("black")
    pensize(1)
    fillcolor("white")
    hideturtle()
    speed(10)


# I embedded the screen setup in the function for drawing the star
def draw_star(a):
    setup_screen()
    d = 400
    setx(- 0.5 * d)
    setheading(0)
    r = a + 180
    pendown()
    begin_fill()
    forward(d) # 2 lines get turtle out of the original heading
    right(r)
    x = 1 # for test_count
    while turtle.heading() != 0:
        forward(d)
        right(r)
        x = x + 1 # for testing i counted the iterations
    end_fill()
    outcome = (p, x, a)
    outcome = str(outcome)
    print(outcome)

#    For testing I used a file to collect data for a while
#    with open('file.txt', 'a') as file:
#        file.write(outcome)
#        file.write('\n')


# And then the script for calculating the angle
# In the test phase I used a list of values for p to test the script
list = [3, 5, 7, 9, 11, 13, 17, 19, 23, 29]
for p in list:
    if p % 2 == 0:
        if p / 2 % 2 == 0:
            a = 360 / p
        else:
            a = 720 / p
    else:
        a = 180 / p
    draw_star(a)

# This code is optional for incidental screensaves 
# ts = turtle.getscreen()
# ts.getcanvas().postscript(file="amhappy7.eps")

