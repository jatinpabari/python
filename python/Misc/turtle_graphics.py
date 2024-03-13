from turtle import Turtle, Screen
import random

def move():
    timmy = Turtle()
    timmy.color("blue")
    timmy.speed('slowest')
    timmy.shape('turtle')
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    # screen = Screen()
    # screen.exitonclick()

def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return (r,g,b)

def draw_spirograph():
    tim = Turtle()
    tim.speed('fastest')
    for _ in range(100):
        tim.circle(100)
        tim.color('blue')
        tim.setheading(tim.heading() + 10)

if __name__ == '__main__':
    move()
    # draw_spirograph()
    screen = Screen()
    screen.exitonclick()



