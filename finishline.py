from turtle import Turtle


class FinishLine(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor('black')
        self.pensize(2)
        self.penup()
        self.goto(-280, 250)
        self.pendown()
        self.forward(550)
        self.hideturtle()
