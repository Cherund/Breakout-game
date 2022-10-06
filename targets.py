from turtle import Turtle


class Targets(Turtle):

    def __init__(self, color, x, y):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x, y)
