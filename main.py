from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Global Variables
bars = []
removed_bars = []

# Starter Screen
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Vaccinate!")
screen.tracer(0)

# Add Image Files to Screen
ball_image= "gif/ball.gif"
paddle_image = "gif/paddle.gif"
screen.addshape(ball_image)
screen.addshape(paddle_image)
for i in range (2,6):
    screen.addshape(f"gif/v{i}.gif")

# Field
def make_field ():
    global bars
    bar = Turtle()
    bar.penup()
    for i in range(2, 6):
        bar.shape(f"gif/v{i}.gif")
        for j in range(1, 11):
            bar.setpos(-400 + (j * 70), -100 + (i * 80))
            a = bar.clone()
            bars.append (a)
            bar.stamp()
            j += 1
    bars.append(bar)

# Score and Messages
player_score = Score()
player_score.score_board()
game_over = Score()
win = Score()

# Paddle
paddle = Paddle()
screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

# Ball
ball = Ball()
ball.setheading(300)

# Game Mechanics
make_field()
game_continue = True
while game_continue:
    time.sleep(.05)
    screen.update()
    current_heading = ball.heading()
    ball.move()

    # Paddle Bounce
    if ball.distance(paddle) <30:
        ball.setheading(current_heading + 175)

    # Wall Bounce
    elif ball.ycor()>375:
        ball.setheading(current_heading + 75)
    elif ball.xcor()>375 or ball.xcor()<-375:
        ball.setheading(current_heading + 90)
    elif ball.ycor()<-375:
        game_over.game_over()
        break

    # Virus Bounce
    elif ball.ycor()>0 and ball.ycor()<375:
        for bar in bars:
            bar.clear()
            if ball.distance(bar) <30:
                bar.setpos(500, 500)
                player_score.points +=1
                player_score.score_board()
                ball.setheading(current_heading + 75)
                removed_bars.append(bar)

    # Winning
    elif len(removed_bars) == 40:
        win.win()
        break

screen.exitonclick()


