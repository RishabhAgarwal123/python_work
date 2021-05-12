from turtle import Turtle
# import random


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed(6)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def refresh(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        # x_cor = random.randint(-350, 350)
        # y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        # Reversing the direction of ball in y direction
        self.y_move *= -1

    def bounce_x(self):
        # Reversing the direction of ball when collision with paddle
        self.x_move *= -1
        # self.move_speed += 0.9

    def reset_ball(self):
        self.goto(0, 0)
        # self.move_speed = 0.1
        self.bounce_x()
