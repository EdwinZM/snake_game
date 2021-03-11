from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

position = 0

for i in range(3):
    cube = Turtle()
    cube.shape("square")
    cube.color("white")
    cube.setx(position)
    position -= 20

screen.exitonclick() 