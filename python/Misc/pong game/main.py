from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('blue')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.move_up, key='Up')
screen.onkey(r_paddle.move_down, key='Down')

screen.onkey(l_paddle.move_up, key='w')
screen.onkey(l_paddle.move_down, key='s')

ball = Ball()

scoreboard = Scoreboard()

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        ball.bounce_x()
        scoreboard.l_point()
    
    #Detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        ball.bounce_x()
        scoreboard.r_point()    

screen.exitonclick()