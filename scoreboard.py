from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


