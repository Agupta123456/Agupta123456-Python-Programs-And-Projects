import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("purple")

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color


# def tim_shapes(num_sides):
#     angles = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angles)
#
# for shapes_side in range(3, 11):
#     tim.color(random.choice(colour))
#     tim_shapes(shapes_side)

direction = [0, 90, 180, 270]

tim.speed("fastest")
tim.pensize(15)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))




screen = Screen()
screen.exitonclick()