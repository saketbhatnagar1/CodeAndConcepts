from turtle import Turtle, Screen
import random

titu = Turtle()
titu.shape("turtle")
titu.color("blue")

colors = [
    (0.9, 0.1, 0.1),
    (0.1, 0.3, 0.9),
    (0.1, 0.8, 0.2),
    (1.0, 0.5, 0.0),
    (0.6, 0.2, 0.7)
]

def drawShapes(num_of_sides):
    angle = 360/num_of_sides
    for i in range(num_of_sides):
        titu.forward(100)
        titu.right(angle)

def move_forward():
    titu.forward(10)

def move_left():
    titu.left(90)

def move_right():
    titu.right(90)

screen = Screen()
screen.listen()

screen.onkey(move_forward, "space")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.exitonclick()
