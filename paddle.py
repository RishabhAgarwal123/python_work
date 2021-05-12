from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.color('white')

    def move_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def move_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
