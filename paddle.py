from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, y_cor):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.sety(y_cor)

    def go_right(self):
        new_x = self.xcor() + 20
        self.setx(new_x)

    def go_left(self):
        new_x = self.xcor() - 20
        self.setx(new_x)
