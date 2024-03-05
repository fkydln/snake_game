from turtle import Turtle
ALIGNMENT = 'left'
FONT = ("Courier", 32, "normal")
class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.score = score
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scoreboard(score)

    def game_over(self):
        self.goto(-80,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self, score):
        self.clear()
        self.penup()
        self.goto(-280, 250)
        self.write(arg=f"Score: {score}", align="left", font=("Courier", 24, "normal"))
