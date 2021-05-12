# Create snake body
from turtle import Turtle
import random
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
COLORS = ['red', 'white', 'blue', 'purple']
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_turtle(position)

    def add_turtle(self, position):
        # turtle_length = len(self.turtles)
        # if turtle_length == 0 or turtle_length % 2 == 1:
        timmy = Turtle(shape='circle')
        # else:
        #     timmy = Turtle(shape="square")
        timmy.color(random.choice(COLORS))
        timmy.penup()
        timmy.goto(position)
        self.turtles.append(timmy)
        if len(self.turtles) > 5:
            timmy.speed(0)

    def reset_snake(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend_snake(self):
        self.add_turtle(self.turtles[-1].position())

    def move(self):
        for turtle_num in range(len(self.turtles) - 1, 0, -1):
            x_position = self.turtles[turtle_num - 1].xcor()
            y_position = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(x_position, y_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
