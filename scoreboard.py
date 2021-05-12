from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, 260)
        self.color('black')
        self.hideturtle()
        self.update_level()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}  FINISH LINE", align='Left', font=FONT)

    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write("GAME OVER.", align='center', font=FONT)