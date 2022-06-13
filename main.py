from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food

sc=Screen()
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title(" SNAKE GAME ")
sc.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()

sc.listen()
sc.onkey(snake.up,"Up")
sc.onkey(snake.down,"Down")
sc.onkey(snake.left,"Left")
sc.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 288 or snake.head.xcor() < -288 or snake.head.ycor() >288 or snake.head.ycor()< -288:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()



sc.exitonclick()





