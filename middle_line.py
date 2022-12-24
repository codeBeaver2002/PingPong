from turtle import *
WIDTH, HEIGHT = 1000, 800
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()

    def create_line(self):
        self.goto(0, -HEIGHT/2)
        self.setheading(90)
        while self.ycor() < HEIGHT/2:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
