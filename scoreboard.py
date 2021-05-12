from turtle import Turtle
POSITION = 'center'
FONT = ('Arial', 14, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        with open('data.txt') as file:
            res = file.read()
            self.high_score = int(res)
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align=POSITION, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0

    # def game_over(self):
    #     self.color('red')
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER ", align=POSITION, font=FONT)
