from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_image = "gif/paddle.gif"
        self.penup()
        self.shape(self.paddle_image)
        self.goto(0, -300)

    def left(self):
        self.setpos(self.xcor()-25, self.ycor())

    def right(self):
        self.setpos(self.xcor()+25, self.ycor())

