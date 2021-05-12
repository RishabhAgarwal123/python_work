import turtle
import pandas

screen = turtle.Screen()
screen.setup(750, 500)
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


# def turtle_on_click(x, y):
#     print(x, y)
# turtle.onscreenclick(turtle_on_click)
# turtle.mainloop()
data = pandas.read_csv('50_states.csv')
states = data.state.to_list()
guesses = []
score = 0


while len(guesses) < 50:
    user_input = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name").capitalize()
    if user_input == 'Exit':
        missing_states = [state for state in states if state not in guesses]
        # for state in states:
        #     if state not in guesses:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_missed.csv")
        print(missing_states)
        break
    if user_input in states:
        guesses.append(user_input)
        score += 1
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state = data[data.state == user_input]
        timmy.goto(int(state.x), int(state.y))
        timmy.write(user_input)
        # timmy.write(state['state'].item())

print(f"Your score is {len(guesses)}")
# screen.exitonclick()
