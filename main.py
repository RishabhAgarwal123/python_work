from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)


left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()
# ball.refresh()


screen.listen()
screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce ball
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        print("Contact with right paddle")
        ball.bounce_x()

    # Ball missed right paddle
    if ball.xcor() > 380:
        scoreboard.left_score_increase()
        ball.reset_ball()

    # Ball missed left paddle
    if ball.xcor() < -380:
        scoreboard.right_score_increase()
        ball.reset_ball()


screen.exitonclick()
