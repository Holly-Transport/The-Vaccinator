from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_img = "gif/ball.gif"
        self.penup()
        self.shape(self.ball_img)

    def move(self):
        self.forward(10)