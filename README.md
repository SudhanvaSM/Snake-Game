# Snake-Game

A classic Snake game built using Python and the Turtle graphics library. In this game, you control a snake that grows longer each time it eats food while avoiding collisions with the walls and itself.

How to Play: 
  1.Run the main.py file to start the game. 
  2.Use the arrow keys to control the snake. 
  3.Try to eat as much food as possible while avoiding collisions!

Features: 
  1.Snake Movement: Control the snake using the arrow keys (↑,↓,→,←) 
  2.Food: Randomly placed food that the snake can eat to grow longer. 
  3.Score Tracking: Displays the current score at the top of the screen, which increases each time the snake eats food. 
  4.Game Over: The game ends if the snake collides with the boundaries or itself, displaying a "Game Over" message. 
  5.Snake Growth: Each time the snake eats food, it grows by one segment. 
  6.Real-Time Gameplay: The game runs in real-time with smooth animations using Turtle’s screen update and time delay functions.

Game Mechanics: 
  1.The game starts with a snake consisting of three segments and an initial score of 0. 
  2.The snake moves according to user input, and each time it eats food, it grows by one segment and the score increases. 
  3.The game ends if the snake hits the walls or collides with its own body.

Files: 
  1.main.py: Main file to run the game, initializes the screen, and handles user input. 
  2.snake.py: Defines the snake's structure, movement, and growth. 
  3.food.py: Handles food placement and randomization on the screen. 
  4.score.py: Manages the score display and updates during the game.
