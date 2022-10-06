from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setpos(0, -250)
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 1
        self.game = True

    def move(self):
        self.goto(self.xcor() + self.x_move*self.move_speed, self.ycor() + self.y_move*self.move_speed)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def position_reset(self):
        self.goto(0, -250)
        self.y_move *= -1
        self.move_speed = 1

    def speed_increase(self, targ_left):
        if targ_left == 108 or targ_left == 100 or targ_left == 56 or targ_left == 28:
            self.move_speed *= 1.3
