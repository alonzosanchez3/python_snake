from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor('black')
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')
screen.listen()

# segment = Turtle()
# segment.shape('square')
# segment.color('white')
screen.update()
game = True
while(game):
  screen.update()
  time.sleep(0.1)
  snake.move_segment()
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
    # snake.create_segments()

  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.reset()
    snake.reset()

  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      scoreboard.reset()
      snake.reset()






screen.exitonclick()