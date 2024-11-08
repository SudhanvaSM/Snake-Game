#Main file where the game executes
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

#Building the screen layout by setting the size, background color and animation.
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Creating the objects for the classes.
snake = Snake()
food = Food()
score = Score()

#Listening to the uesr's input to move the snake accordingly.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

#Run the game
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Check if the snake ate the food
    if snake.head.distance(food) < 15:
        food.new_food_location()
        snake.extend_segment()
        score.increase_score()

    #Check if the snake colloides with the boundary of the game.
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_is_on = False
        score.display_game_over()

    #Check if the snake collides with itself.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.display_game_over()

screen.exitonclick()