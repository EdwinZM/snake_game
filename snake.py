from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
    
    def extend(self):
        position_x = self.cubes[-1].xcor()
        position_y = self.cubes[-1].ycor()
        self.cube = Turtle()
        self.cube.shape("square")
        self.cube.color("white")
        self.cube.penup()
        self.cube.goto(position_x, position_y)
        self.cubes.append(self.cube)

    def move(self):
        for i in range(len(self.cubes) -1, 0, -1):
            new_x = self.cubes[i - 1].xcor()
            new_y = self.cubes[i - 1].ycor()
            self.cubes[i].goto(new_x, new_y)
    def up(self):
        if self.cubes[0].heading() != DOWN:
            self.move()
            self.cubes[0].setheading(UP)
            self.cubes[0].forward(20)

    def down(self):
        if self.cubes[0].heading() != UP:
            self.move()
            self.cubes[0].setheading(DOWN)
            self.cubes[0].forward(20)

    def left(self):
        if self.cubes[0].heading() != RIGHT:
            self.move()
            self.cubes[0].setheading(LEFT)
            self.cubes[0].forward(20)

    def right(self):
        if self.cubes[0].heading() != LEFT:
            self.move()
            self.cubes[0].setheading(RIGHT)
            self.cubes[0].forward(20)
        
        