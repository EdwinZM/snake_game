from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    #time.sleep(0.1)
    if snake.cubes[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    
    if snake.cubes[0].xcor() > 280 or snake.cubes[0].xcor() < -280 or snake.cubes[0].ycor() < -280 or snake.cubes[0].ycor() > 280:
        game_is_on = False
        score.game_over()
    
    for i in snake.cubes[1:]:
        if snake.cubes[0].distance(i) < 10:
            game_is_on = False
            score.game_over()
            
        

screen.exitonclick() 