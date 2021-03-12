from turtle import Turtle

class Snake:
    def __init__(self):
        position = 0

        self.cubes = []

        for i in range(3):
            self.cube = Turtle()
            self.cube.shape("square")
            self.cube.color("white")
            self.cube.penup()
            self.cube.goto(position, 0)
            position -= 20
            self.cubes.append(self.cube)
    
    def move(self):
        for i in range(len(self.cubes) -1, 0, -1):
            new_x = self.cubes[i - 1].xcor()
            new_y = self.cubes[i - 1].ycor()
            self.cubes[i].goto(new_x, new_y)
        self.cubes[0].forward(20)
        self.cubes[0].left(90)
        