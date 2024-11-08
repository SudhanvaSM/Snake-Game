#Defines the food and its structure all while randomizing it's location.
from turtle import Turtle
import random

class Food(Turtle):

    #Define the food size,color and coordinates.
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.color('red')
        self.speed('fastest')
        self.new_food_location()

    #Randomize the location of the food within the 600x600 pixel boundary.
    def new_food_location(self):
        x_cor = random.randint(-280,280)
        y_cor = random.randint(-280,280)
        self.goto(x_cor,y_cor)