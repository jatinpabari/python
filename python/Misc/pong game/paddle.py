from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto((position))


    def move_up(self):
        new_y = self.ycor() + 20
        self.penup()
        self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y = self.ycor() - 20
        self.penup()
        self.goto(self.xcor(), new_y)