from turtle import Turtle

STARTING_POS = [(0,0), (-20,0),(-40,0) ]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for pos in STARTING_POS:
            part = Turtle("square")
            part.shapesize(stretch_wid=0.5, stretch_len=0.5)
            part.color("white")
            part.penup()
            part.goto(pos)
            self.parts.append(part)
    
    def stretch_snake(self):
        part = Turtle("square")
        part.shapesize(stretch_wid=0.5, stretch_len=0.5)
        part.color("white")
        part.penup()
        part.goto(self.parts[-1].position())
        self.parts.append(part)

    def move(self):
        for part in range(len(self.parts)-1, 0, -1):
            x_cor = self.parts[part-1].xcor()
            y_cor = self.parts[part-1].ycor()
            self.parts[part].goto(x_cor, y_cor)
        
        self.parts[0].forward(MOVE_DISTANCE)

    def up(self):
        self.parts[0].setheading(90)
    
    def down(self):
        self.parts[0].setheading(270)

    def left(self):
        self.parts[0].setheading(180)

    def right(self):
        self.parts[0].setheading(0)
