# A python script to test the turtle module
from turtle import *
from random import *
from math import *
from numpy import *


def triangle_octagon():

    # select number of sides/vertices
    while True:
        try:
            num_vert = int(input("Pick a number between 3 - 8: ").strip())

            if 3 <= num_vert <=8:
                break
            else:
                print("Please pick a number between 3 - 8 only")

        except ValueError:
            print("insert numbers only")

    # turtle create
    turtle = Turtle()
    turtle.shape('turtle')

    # create fill color (fill color is dependent on whether num_vert is even or odd
    colors = ['red', 'blue']
    turtle.color('black', colors[num_vert % 2])

    # turtle movement (exterior angles of all polygons add up to 360 degrees)
    turtle.begin_fill()
    for _ in range(num_vert):
        turtle.forward(100)
        turtle.left(360/num_vert)
    turtle.end_fill()

    done()
    return


def flower():
    # create turtle
    turtle = Turtle()
    turtle.shape('arrow')
    turtle.color('red', 'yellow')

    # turtle movement
    turtle.begin_fill()
    for _ in range(25):
        turtle.forward(200)
        turtle.left(165)
    turtle.end_fill()

    done()
    return


def stars(num_sets, num_stars):
    try:
        # set up screen
        screensize(canvwidth=500, canvheight=500)

        # create turtle
        turtle = Turtle()
        turtle.shape('arrow')
        colors = ['red', 'green', 'blue']
        turtle.speed(5)

        # turtle movement
        for n in range(num_sets):
            turtle.teleport(randint(-200, 200), y=randint(-200,200))
            for i in range(num_stars):
                turtle.fillcolor(colors[i % len(colors)])
                turtle.begin_fill()
                for _ in range(5):
                    turtle.forward(100)
                    turtle.left(216)
                turtle.end_fill()
                turtle.left(360/num_stars)

        done()
        return

    except TypeError:
        print("Only enter integers as arguments")
        return


# this function will be used within the mathematical function
def my_function(x):
    # edit the line below to change the output of mathematical_function()
    return sin(radians(x))


def mathematical_function(start_value, end_value, x_scale, y_scale):
    """
    A function designed to plot (continuous) functions using the turtle module. Edit the function above
    (my_function()) in order to change the graph sketched. This function is limited in what it can do.
    It requires the user to tinker the functions 4 arguments in order for a graph to be properly sketched.
    Non-continuous functions will not be sketched properly.
    """

    # set screen size
    screensize(canvwidth=800, canvheight=800)

    # set up turtle
    pen = Turtle()
    pen.shape('classic')
    pen.pensize(1)
    pen.speed(5)

    # draw graph axes
    pen.up()
    pen.goto(-300,0)
    pen.down()
    pen.goto(300,0)
    pen.up()
    pen.goto(0,-300)
    pen.down()
    pen.goto(0,300)
    pen.up()
    pen.home()

    # change pen color/size
    pen.color('red')
    pen.pensize(2)

    # Move to starting position
    pen.goto(start_value * x_scale, my_function(start_value) * y_scale)

    # draw sqrt graph between 0 and 200 pixels
    pen.down()
    for x in arange(start_value, end_value, 0.3):
        pen.goto(x * x_scale,my_function(x) * y_scale)

    done()
    return


def spiral():
    colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    # set up turtle/screen
    pen = Turtle()
    pen.shape('classic')
    bgcolor('black')
    pen.speed(60)

    # turtle movement
    for x in range(300):
        pen.pencolor(colours[x % 6])
        pen.forward(x)
        pen.left(59)


    done()
    return
    

# chose a function to run here
if __name__ == "__main__":
    spiral()