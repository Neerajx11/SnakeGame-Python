from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.update()
        self.writeScore()

    def update(self):
        self.score += 1
        self.writeScore()

    def writeScore(self):
        self.goto(0, 260)
        self.clear()
        self.color("white")
        self.write(f'Score : {self.score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
