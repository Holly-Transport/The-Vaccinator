from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.points = 0
        self.color("white")
        self.hideturtle()

    def score_board(self):
        self.clear()
        self.setpos(-350,350)
        self.write(f"Score: {self.points}", align="left", font=("Open Sans", 25, "normal"))

    def game_over(self):
        self.clear()
        self.setpos(0,-100)
        self.color("white")
        self.write(f"GAME OVER", align="center", font=("Open Sans", 60, "normal"))

    def win(self):
        self.clear()
        self.setpos(0,-100)
        self.color("white")
        self.write(f"YOU STOPPED THE PANDEMIC!", align="center", font=("Open Sans", 60, "normal"))