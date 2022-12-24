from turtle import *
WIDTH, HEIGHT = 1000, 800

ALIGNMENT = "center"
FONT = ("Courier", 40, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.rscore = 0
        self.lscore = 0
        self.update_score_board()



    def update_score_board(self):
        self.clear()
        self.goto(-100, HEIGHT / 2 - 60)
        self.write(self.lscore, move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, HEIGHT / 2 - 60)
        self.write(self.rscore, move=False, align=ALIGNMENT, font=FONT)


    def updateScoreRight(self):
        self.rscore = self.rscore + 1

    def updateScoreLeft(self):
        self.lscore = self.lscore + 1
