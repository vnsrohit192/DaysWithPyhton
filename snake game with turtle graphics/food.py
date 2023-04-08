from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1,1)
        self.color("yellow")
        self.refresh()
    def refresh(self):
        self.goto(random.randint(-200,200), random.randint(-200,200))

    
     




