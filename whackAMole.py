#Matt Westelman
#4/4/18
#whackAMOle.py - My first big project

from ggame import *
from random import randint

#what happens when you click the mouse
#def mouseClick(event): 
    
def moveMole():
    data['frames'] = 0 #reset the tp timer
    holeNum = randint(1,6)
    if holeNum==1:
        mole.x = 30
        mole.y = 50
    elif holenum==2:
        mole.x = 200
        mole.y = 50
    elif holenum==3:
        mole.x = 370
        mole.y = 50
    elif holenum==4:
        mole.x = 30
        mole.y = 200
    elif holenum==5:
        mole.x = 200
        mole.y = 200
    else:
        mole.x = 370
        mole.y = 200
     

#Updating score
    def updateScore(): 
        data['score'] += 10
        data['scoreText'].destroy() #remove old writing
        scoreBox = TextAsset('Score = '+str(data['score']))


#Keeps track of how many frames since last teleport, and TPs it after 10 frames
def step():
    data['frames'] +=1
    if data['frames']%10 == 0:
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
    mole = CircleAsset(70, LineStyle(1,black),brown)
    
    
    Sprite(moleHill, (30,50))
    Sprite(moleHill, (200,50))
    Sprite(moleHill, (370,50))
    Sprite(moleHill, (30,200))
    Sprite(moleHill, (200,200))
    Sprite(moleHill, (370,200))
    Sprite(mole)

#This activates the click part
    #App().listenMouseEvent('click', mouseClick) 
    App().run(step)

