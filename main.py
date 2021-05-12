from turtle import Turtle, Screen
import random

x_cordinate = -230
y_cordiante = -170
is_race_start = False


screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter the color").lower()
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
turtle_list = []


for item in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[item])
    x_cordinate = x_cordinate
    y_cordiante = y_cordiante + 50
    timmy.goto(x=x_cordinate, y=y_cordiante)
    turtle_list.append(timmy)


if user_choice:
    is_race_start = True


while is_race_start:
    for turtle in turtle_list:
        if turtle.xcor() > 200:
            is_race_start = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You WON !, The {winning_color} turtle is the winner.")
            else:
                print(f"You LOSE !, The {winning_color} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
