from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=500)
user_guess = screen.textinput(title="Place a bet", prompt="Which color will win the race? (Red/Green/Blue/Black/Yellow)?")

all_turtles = []

red = Turtle()
red.penup()
red.goto(x=-230, y=10)
red.shape('turtle')
red.color('red')
all_turtles.append(red)

blue = Turtle()
blue.penup()
blue.goto(x=-230, y=40)
blue.shape('turtle')
blue.color('blue')
all_turtles.append(blue)

black = Turtle()
black.penup()
black.goto(x=-230, y=70)
black.shape('turtle')
black.color('black')
all_turtles.append(black)

green = Turtle()
green.penup()
green.goto(x=-230, y=-20)
green.shape('turtle')
green.color('green')
all_turtles.append(green)

yellow = Turtle()
yellow.penup()
yellow.goto(x=-230, y=-50)
yellow.shape('turtle')
yellow.color('yellow')
all_turtles.append(yellow)

is_race_on = False

if user_guess is not None:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_guess:
                print(f'You have won! {winning_color} has won')
            else:
                print(f'You have lost! {winning_color} has won')
        r = random.randint(0, 15)
        t.forward(r)

screen.exitonclick()
