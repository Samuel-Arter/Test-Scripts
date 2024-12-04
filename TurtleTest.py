# A python script to test the turtle module
from turtle import *


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

# chose a function to run
if __name__ == "__main__":
    flower()