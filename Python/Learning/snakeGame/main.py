from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600,height = 600)



starting_positions = [(0,0),(-20,0),(-40,0)]
segment_1 = Turtle("square")
segment_1.color("white")
segment_2 = Turtle("square")
segment_2.color("white")
segment_3 = Turtle("square")
segment_3.color("white")





screen.bgcolor("black")
screen.title("My snake game")
screen.exitonclick()