from turtle import Turtle

Font="Arial"
Fontsize=20
Char_specification="normal"
# with open("data.txt")as file:
#     Highscore=int(file.read())
# with open("data.txt","w") as file:
#     file.write(Highscore)  
import food
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.penup()
        self.color("red")
        self.goto(0,270)
        self.hideturtle()
        self.updatescoreboard()
        
    def updatescoreboard(self):
        self.clear()
        self.write(f"score:{self.score} High Score: {self.highscore}",align="center",font=(Font,Fontsize,Char_specification))

    def changescore(self):
        self.score+=1    
        self.updatescoreboard()

    def reset(self):
        if self.score>self.highscore:
                self.highscore=self.score
                with open("data.txt","w") as data:
                   data.write(f"{self.highscore}")
        self.highscore=self.score
        self.score=0
        self.updatescoreboard()


            

    