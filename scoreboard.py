
from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()


    def add_point(self):
        self.score += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over",  align="center", font=("Arial", 24, "normal"))