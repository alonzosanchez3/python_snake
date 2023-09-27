from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
  def __init__(self):
    self.segments = []
    self.create_segments()
    self.head = self.segments[0]

  def create_segments(self):
    x = 20
    for i in range(3):
      segment = Turtle()
      segment.shape('square')
      segment.color('white')
      segment.penup()
      segment.pensize(20)
      segment.setpos(x,0)
      self.segments.append(segment)
      x -= 20

  def create_segment(self, position):
    segment = Turtle()
    segment.shape('square')
    segment.color('white')
    segment.penup()
    segment.pensize(20)
    segment.goto(position)
    self.segments.append(segment)

  def extend(self):
    self.create_segment(self.segments[-1].position())

  def move_segment(self):
    for i in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[i - 1].xcor()
      new_y = self.segments[i - 1].ycor()
      self.segments[i].goto(new_x, new_y)
    self.segments[0].forward(20)

  def up(self):
    if(self.head.heading() != DOWN):
      self.head.setheading(90)

  def down(self):
    if(self.head.heading() != UP):
      self.head.setheading(270)

  def right(self):
    if(self.head.heading() != LEFT):
      self.head.setheading(0)

  def left(self):
    if(self.head.heading() != RIGHT):
      self.head.setheading(180)
