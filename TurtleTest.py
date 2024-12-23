# A python script to test the turtle module
from turtle import *
from random import *
from math import *


def triangle():
    # create turtle
    turtle = Turtle()
    turtle.color('red')
    turtle.shape('turtle')

    # turtle movement
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

    done()
    return


def square():
    # create turtle
    turtle = Turtle()
    turtle.shape('turtle')

    # turtle movement
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

    done()
    return


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
    return x ** 2


def mathematical_function(start_value, end_value):

    # set screen size
    screensize(canvwidth=500, canvheight=500)

    # set up turtle
    pen = Turtle()
    pen.shape('classic')
    pen.pensize(1)

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

    # Find starting y-coordinate for function:
    y_coordinate = my_function(start_value)

    # draw sqrt graph between 0 and 200 pixels
    pen.down()
    for x in range(-start_value, end_value + 1):
        pen.goto(x,my_function(x))


    done()
    return
    

# chose a function to run here
if __name__ == "__main__":
    mathematical_function()