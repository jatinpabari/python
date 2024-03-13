import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'C:\\Users\\jatin\\Code Zone\\visual studio code\\python\\US States Game\\blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)


data = pandas.read_csv('C:\\Users\\jatin\\Code Zone\\visual studio code\\python\\US States Game\\50_states.csv')
# print(data.state)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) <  50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct", prompt="What's another state name?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        # print(int(state_data.x))
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()