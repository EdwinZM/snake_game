from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.sety(260)
        self.color("white")
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.score += 1

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
