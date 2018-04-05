#Matt Westelman
#4/4/18
#whackAMOle.py - My first big project

from ggame import *
from random import randint

ROWS = 6
COLS = 6
CELL_SIZE = 50

#what happens when you click the mouse
def mouseClick(event): 

def moveMole():
    data['frames'] = 0 #reset the tp timer

#Updating score
    def updateScore(): 
        data['score'] += 10
        data['scoreText'].destroy() #remove old writing
        scoreBox = TextAsset('Score = '+str(data['score']))


#Keeps track of how many frames since last teleport, and TPs it after 150 frames
def step():
    data['frames'] +=1
    if data['frames']%150 == 0:
        moveMole()

#Sets up and runs game 
if __name__ == '__main__':
    
     #hold variable in dictionary
    data = {}
    data['score'] = 0
    data['frames'] = 0
    
    #colors for the color god
    brown = Color(0x8B4513,1)
    black = Color(0x000000,1) #Black
    
    #graphics for the graphic throne
    moleHill = CircleAsset(70, LineStyle(1,black),black)
    
    
    
    Sprite(moleHill, (30,50))

#This activates the click part
    App().listenMouseEvent('click', mouseClick) 
    App().run()

