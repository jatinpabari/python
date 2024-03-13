from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

starting_pos = [(0,0), (-20,0),(-40,0) ]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        print('food almost there')
        food.refresh()
        scoreboard.update_score()
        snake.stretch_snake()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        print('wall almost there')
        game_on = False
        scoreboard.finish_game()

    # Detect collision with any part of snake
    
    for part in snake.parts:
        if part != snake.head and snake.head.distance(part) < 10:
            print('collision with snake body')
            game_on = False
            scoreboard.finish_game()

    
    
        
    

screen.exitonclick()