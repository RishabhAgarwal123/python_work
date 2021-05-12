from turtle import Turtle
POSITION = 'center'
FONT = ('Courier', 80, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.left_score, align=POSITION, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=POSITION, font=FONT)

    def left_score_increase(self):
        self.left_score += 1
        self.clear()
        self.update_score()

    def right_score_increase(self):
        self.right_score += 1
        self.clear()
        self.update_score()


