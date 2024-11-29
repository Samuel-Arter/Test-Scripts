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

def polygon():
    # create turtle
    turtle = Turtle()
    turtle.shape('turtle')

    # select number of sides/vertices
    while True:
        try:
            num_vert = input(int("Pick a number between 3 - 8: ").strip())

            if num_vert < 3 or num_vert > 3:
                print("Please pick a number between 3 - 8 only")
            else:
                break

        except ValueError:
              print("insert numbers only")

    # turtle movement
    for _ in range(num_vert):





# chose a function to run
if __name__ == "__main__":
    square()