# A python script to test the turtle module
from turtle import *


def triangle():
    # create turtle
    turtle = Turtle()
    turtle.color('red')
    turtle.shape('turtle')

    # turtle movement
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(45)

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

    # turtle movement (exterior angles of polygon always add up to 360 degrees)
    for _ in range(num_vert):
        turtle.forward(100)
        turtle.left(360/num_vert)

    done()
    return



# chose a function to run
if __name__ == "__main__":
    triangle_octagon()