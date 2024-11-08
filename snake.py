#Defines the snake by creating atleast 3 segments and moves it according to user's input.
from turtle import Turtle

#Initialise the starting coordiantes of three segments/the snake.
START_POS = [(0,0), (-20,0), (-40,0)]

#Define the values of each direction.
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #Create the starting segments using the starting coordinates.
    def create_snake(self):
        for position in START_POS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    #Every time the snake eats food, it's length should increase.
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    #Adding the new segment of snake after it gains a point.
    def extend_segment(self):
        self.add_segment(self.segments[-1].position())
    
    #Make the snake move all the segments together as one unit.
    def move(self):
        for seg_num in range (len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
    
        self.head.forward(MOVE_DISTANCE)

    #Move the snake in upward direction.
    def up(self):
        #If the snake is facing down, it cannot go up and vice-versa.
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    #Move the snake in downward direction.
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    #Move the snake toward left.
    def left(self):
        #If the snake is facing toward right, it cannot go left and vice-versa.
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    #Move the snake toward right.
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


