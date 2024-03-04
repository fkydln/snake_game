from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.score = score
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard(score)

    def update_scoreboard(self, score):
        self.clear()
        self.penup()
        self.goto(-280, 250)
        self.write(arg=f"Score: {score}", align="left", font=("Courier", 24, "normal"))
