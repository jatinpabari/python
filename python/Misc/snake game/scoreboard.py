from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('C:\\Users\\jatin\\Code Zone\\visual studio code\\python\\Misc\\snake game\\high_score.txt', mode='r+') as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f'Score {self.score} High Score {self.high_score}', align="center", font=('Arial', 20, "bold"))
        self.hideturtle()

    def update_score(self):
        self.score = self.score + 1
        self.clear()
        self.write(f'Score {self.score}. High Score {self.high_score}', align="center", font=('Arial', 20, "bold"))


    def finish_game(self):
        self.goto(0, 0)
        self.write(f'GAME OVER!!!', align="center", font=('Arial', 20, "bold"))
        if(self.score > int(self.high_score)):
            self.high_score = self.score
            with open('C:\\Users\\jatin\\Code Zone\\visual studio code\\python\\Misc\\snake game\\high_score.txt', mode='w+') as file:
                file.write(str(self.high_score))
        