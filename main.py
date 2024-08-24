from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Detect collisions with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.add_point()
        snake.extend_snake()
        
    # Detect collisions with wall
    x_coord = snake.head.xcor()
    y_coord = snake.head.ycor()
    if x_coord > 290 or x_coord < -290 or y_coord > 290 or y_coord < -290:
        game_is_on = False
        scoreboard.game_over()


    # Detect collisions with tail
    for segment in snake.body[1:]:

        if segment is not snake.head and snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    
screen.exitonclick()