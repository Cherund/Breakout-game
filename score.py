from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score_points = 0
        self.lives_left = 3
        self.update()
        self.game = True

    def update(self):
        self.clear()
        self.goto(-230, 400)
        self.write(f'Score:{self.score_points}', align='center', font=('Arial', 40, 'normal'))
        self.goto(230, 400)
        self.write(f'Lives:{self.lives_left}', align='center', font=('Arial', 40, 'normal'))

    def score(self, color):
        if color[0] == 'yellow':
            self.score_points += 1
        elif color[0] == 'green':
            self.score_points += 3
        elif color[0] == 'orange':
            self.score_points += 5
        elif color[0] == 'red':
            self.score_points += 7
        self.update()

    def lives(self):
        self.lives_left -= 1
        if self.lives_left != 0:
            self.update()
        else:
            self.goto(0, 0)
            self.write('GAME OVER!', align='center', font=('Arial', 60, 'normal'))
            self.game = False

    def exit_game(self):
        self.game = False
