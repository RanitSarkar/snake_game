from turtle import Turtle
import random

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE= 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
COLOR=["red","green","blue","cyan","yellow","pink","deep pink","violet"]

class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        tim = Turtle("square")
        tim.color(random.choice(COLOR))
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def reset(self):
        for sef in self.segments:
            sef.goto(1000,100)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)