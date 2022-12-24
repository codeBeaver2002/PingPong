from turtle import *
import random
from paddle import *
WIDTH, HEIGHT = 1000, 800
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 5
        self.y_move = 5


    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)


    def not_in_range_right(self):
        if self.xcor() < WIDTH/2:
            return 0
        else:
            game_over = Turtle()
            game_over.color("white")
            game_over.hideturtle()
            # game_over.write("Game Over.\nLeft Wins!!!", align="center", font=("Helvetica",30))
            return 1

    def not_in_range_left(self):
        if self.xcor() > -WIDTH / 2:
            return 0
        else:
            game_over = Turtle()
            game_over.color("white")
            game_over.hideturtle()
            # game_over.write("Game Over.\nRight Wins!!!", align="center", font=("Helvetica",30))
            return 1

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()