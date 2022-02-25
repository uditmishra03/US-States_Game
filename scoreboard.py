from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        # self.update_scoreboard()

    def update_scoreboard(self):
        # self.clear()
        self.score += 1
        # self.write(f"Score: {self.score},", align=ALIGNMENT, font=FONT)

    # def increase_score(self):
    #     self.score += 1
    #     self.update_scoreboard()
