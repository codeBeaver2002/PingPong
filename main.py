import time
import pygame
from turtle import Screen
from paddle import *
from ball import Ball
WIDTH, HEIGHT = 1000, 800
from middle_line import *
from score_board import *
clock = pygame.time.Clock()
clock.tick(60)
def stop():
    game_over = Turtle()
    game_over.color("white")
    game_over.hideturtle()
    if score.lscore > score.rscore:
        game_over.write("Game Over.\n Left Wins!!!", align="center", font=("Helvetica",30))
    elif score.lscore < score.rscore:
        game_over.write("Game Over.\nRight Wins!!!", align="center", font=("Helvetica",30))
    else:
        game_over.write("Game Over.\n    Draw!!!", align="center", font=("Helvetica",30))

    screen.exitonclick()

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


line = Line()
line.create_line()


paddle_right = Paddle(WIDTH/2 - 50 , 0)
paddle_left = Paddle(-WIDTH/2 + 50 , 0)

ball = Ball()

score = Score()


screen.listen()
screen.onkey(key="Up", fun=paddle_right.Up)
screen.onkey(key="Down", fun=paddle_right.Down)

screen.onkey(key="w", fun=paddle_left.Up)
screen.onkey(key="s", fun=paddle_left.Down)

game_is_on = 1

screen.onkey(key="p", fun=stop)
speed_up = 0.01
while game_is_on:
    screen.update()
    if ball.not_in_range_right():
        score.updateScoreLeft()
        score.update_score_board()
        speed_up = 0.01
        ball.reset_position()
    elif ball.not_in_range_left():
        score.updateScoreRight()
        score.update_score_board()
        speed_up = 0.01
        ball.reset_position()
    ball.move()
    time.sleep(speed_up)
    if ball.ycor() > HEIGHT/2 - 10 or ball.ycor() < -HEIGHT/2 + 10:
        ball.bounce_y()
    if ball.distance(paddle_right) < 70 and ball.xcor() == WIDTH/2 - 75:
        ball.bounce_x()
        speed_up -= 0.001
    if ball.distance(paddle_left) < 70 and ball.xcor() == -WIDTH/2 + 75:
        ball.bounce_x()
        speed_up -= 0.001



