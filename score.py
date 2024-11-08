#This file keeps track of the score and increments it by 1 for every successful attempt.
from turtle import Turtle

#Defining a global varialbe for alignment and font to modify it's value later.
ALIGN = 'center'
FONT = ('arial',20,'normal')

class Score(Turtle):
    
    #Sets up a scoreboard display at the top of the screen with an initial score of 0.
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.hideturtle()
        self.write(f"Score: {self.score}", align = ALIGN ,font=FONT)

    #Updates the scoreboard.
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGN,font = FONT)

    #Increments the scoreboard every time the snake eats the food.
    def increase_score(self):
        self.score += 1
        self.update_score()

    #Displays Game Over.
    def display_game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!",align = ALIGN, font = FONT)