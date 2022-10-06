from turtle import Screen
from paddle import Paddle
from ball import Ball
from targets import Targets
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(650, 900)
screen.title("Breakout")
screen.tracer(0)

target_y = 340
colors = ['red', 'red', 'orange', 'orange', 'green', 'green', 'yellow', 'yellow']
targets = []

for color in colors:
    target_x = -300
    for i in range(14):
        targets.append(Targets(color, target_x, target_y))
        target_x += 45
    target_y += -25

ball = Ball()
paddle = Paddle(-400)
score = Score()
screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')
screen.onkey(score.exit_game, 'space')

while score.game:
    ball.move()
    screen.update()

    for target in targets:
        if ball.distance(target) < 30:
            score.score(target.color())
            target.color('black')
            targets.remove(target)
            ball.bounce_y()
            ball.speed_increase(len(targets))

    if ball.xcor() >= 315 or ball.xcor() <= -315:
        ball.bounce_x()

    if ball.distance(paddle) < 50 and ball.ycor() < -380 or ball.ycor() >= 440:
        ball.bounce_y()

    if ball.ycor() < -440:
        ball.position_reset()
        score.lives()

screen.exitonclick()
