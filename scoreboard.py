from turtle import Turtle

ALIGNMENT = 'left'
FONT = ("Courier", 32, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            print("IN")
            self.high_score = self.score
            print("INNER")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(-80,0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="left", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
