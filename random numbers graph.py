import turtle
import random

win = turtle.Screen()
win.bgcolor("black")
win.title("Practice")
win.tracer(0)
win.setup(600, 600)
win.screensize(600, 600)

x = -270

head = turtle.Turtle()
head.shape("square")
head.color("white")
head.speed(0)
head.penup()
head.goto(-270, 0)
head.direction = "stop"
head.shapesize(0.5, 0.5)

while True:
    win.update()
    while x <= 270:
        head.pendown()
        y = random.randint(-270, 270)
        head.goto(x, y)
        x += 0.05
    win.mainloop()