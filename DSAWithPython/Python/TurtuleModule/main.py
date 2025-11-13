from turtle import Turtle, Screen
import random
titu = Turtle()
titu.shape("turtle")
titu.color("blue")
# titu.forward(100)
# titu.right(90)
# titu.forward(100)
# titu.right(90)
# titu.forward(100)
# titu.right(90)
# titu.forward(100)

#Draw a dashed Line
# for i in range(500):
#     if i%2 == 0:
#         titu.forward(10)
#         titu.pendown()
#     else:
#         titu.forward(10)
#         titu.penup()



#Draw Shapes:
colors = [
    (0.9, 0.1, 0.1),   # red-ish
    (0.1, 0.3, 0.9),   # blue-ish
    (0.1, 0.8, 0.2),   # green-ish
    (1.0, 0.5, 0.0),   # orange
    (0.6, 0.2, 0.7)    # purple
]

def drawShapes(num_of_sides):
    angle = 360/num_of_sides
    for i in range(num_of_sides):
        titu.forward(100)
        titu.right(angle=angle)

        

for i in range(3,7):
    titu.color ( colors[random.randint(0,4)])
    drawShapes(i)









screen = Screen()
screen.exitonclick()
