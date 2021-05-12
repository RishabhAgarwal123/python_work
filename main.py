from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)


# Create snake body
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
# x = 0
# for _ in range(3):
#     timmy = Turtle("square")
#     timmy.color("white")
#     timmy.penup()
#     timmy.goto(x, 0)
#     turtles.append(timmy)
#     x -= 20


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    # for turtle_num in range(start=2, stop=0, step=-1):
    # Move Snake
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend_snake()
        food.refresh()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # score.game_over()
        # print("You lose! ")
        score.reset()
        snake.reset_snake()

    # Detect Collision with tail
    for turtle in snake.turtles[1:]:
        # if turtle == turtle.head:
        #     pass
        if snake.head.distance(turtle) < 10:
            score.reset()
            snake.reset_snake()
            # game_is_on = False
            # score.game_over()


screen.exitonclick()
