#Matt Westelman
#4/4/18
#whackAMOle.py - My first big project

from ggame import *
from random import randint

    
def moveMole():
    print("hello")
    data['frames'] = 0 #reset the tp timer
    holeNum = randint(1,6)
    if holeNum==1:
        mole.x = 30
        mole.y = 50
    elif holeNum==2:
        mole.x = 200
        mole.y = 50
    elif holeNum==3:
        mole.x = 370
        mole.y = 50
    elif holeNum==4:
        mole.x = 30
        mole.y = 200
    elif holeNum==5:
        mole.x = 200
        mole.y = 200
    else:
        mole.x = 370
        mole.y = 200
    return(holeNum)

#what happens when you click the mouse

def mouseClick(event):
    if event.x<=181 and event.y<=191: #and holeNum==1:
        print("Yeet")
    elif event.x>=181 and event.x<=355 and event.y<=191: 
        print("Yo")
    elif event.x>=356 and event.y<=191: 
        print("bro")
    elif event.x<=181 and event.y>=192:
        print("What?")
    elif event.x>=181 and event.x<=355 and event.y>=192:
        print("Hooya!")
    else:
        print("Hoorah!")



#Updating score
def updateScore(): 
    data['score'] += 10
    data['scoreText'].destroy() #remove old writing
    scoreBox = TextAsset('Score = '+str(data['score']))
"""
    def missScore(): 
        data['score'] -= 5
        data['scoreText'].destroy() #remove old writing
        scoreBox = TextAsset('Score = '+str(data['score']))
"""

#Keeps track of how many frames since last teleport, and TPs it after 10 frames
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
    moleAsset = CircleAsset(70, LineStyle(1,black),brown)
    #gague = LineAsset(50,160,blackOutline)
    
    
    Sprite(moleHill, (30,50))
    Sprite(moleHill, (200,50))
    Sprite(moleHill, (370,50))
    Sprite(moleHill, (30,200))
    Sprite(moleHill, (200,200))
    Sprite(moleHill, (370,200))
    mole = Sprite(moleAsset, (30,50))

#This activates the click part
    App().listenMouseEvent('click', mouseClick) 
    App().run(step)
