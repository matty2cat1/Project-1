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
    data['holeNum']=holeNum

#what happens when you click the mouse

def mouseClick(event):
    if event.x<=181 and event.y<=191: 
        print("Yeet")
        if data['holeNum']==1:
            updateScore()
        else:
            missScore()
    elif event.x>=181 and event.x<=355 and event.y<=191: 
        print("Yo")
        if data['holeNum']==2:
            updateScore()
        else:
            missScore()
    elif event.x>=356 and event.y<=191: 
        print("bro")
        if data['holeNum']==3:
            updateScore()
        else:
            missScore()
    elif event.x<=181 and event.y>=192:
        print("What?")
        if data['holeNum']==4:
            updateScore()
        else:
            missScore()
    elif event.x>=181 and event.x<=355 and event.y>=192:
        print("Hooya!")
        if data['holeNum']==5:
            updateScore()
        else:
            missScore()
    else:
        print("Hoorah!")
        if data['holeNum']==6:
            updateScore()
        else:
            missScore()



#Updating score
def updateScore(): 
    data['score'] += 10
    data['scoreText'].destroy() #remove old writing
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(550,50))
    

def missScore(): 
    data['score'] -= 5
    data['scoreText'].destroy() #remove old writing
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(550,50))


#Keeps track of how many frames since last teleport, and TPs it after 10 frames
def step():
    data['frames'] +=1
    if data['frames']%50 == 0:
        moveMole() 

#Sets up and runs game 
if __name__ == '__main__':
    
     #hold variable in dictionary
    data = {}
    data['score'] = 0
    data['frames'] = 0
    data['holeNum'] = 1
    
    #colors for the color god
    brown = Color(0x8B4513,1)
    black = Color(0x000000,1) #Black
    
    #graphics for the graphic throne
    moleHill = CircleAsset(70, LineStyle(1,black),black)
    moleAsset = CircleAsset(70, LineStyle(1,black),brown)
    scoreBox = TextAsset('Score = 0')
    
    
    Sprite(moleHill, (30,50))
    Sprite(moleHill, (200,50))
    Sprite(moleHill, (370,50))
    Sprite(moleHill, (30,200))
    Sprite(moleHill, (200,200))
    Sprite(moleHill, (370,200))
    mole = Sprite(moleAsset, (30,50))
    data['scoreText'] = Sprite(scoreBox,(550,50))

#This activates the click part
    App().listenMouseEvent('click', mouseClick) 
    App().run(step)
