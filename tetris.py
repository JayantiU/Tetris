#tetris.py
#Jayanti Upadhyay
#This is a game of tetris where user's objective is to create a row
#without any gaps.


#TO DO LIST:
# rotation check
# put together game function (main function where game is actually played) + debug 
# add pause, finish instructions and settings page


#-----IMPORTS-----#
from pygame import * 
from random import *
from pprint import pprint 
#-----SCREEN SETUP-----#
screen=display.set_mode((1000,700))
screen.fill((55,55,55))

font.init()


grid=[[0 for i in range(16)] for j in range(20)]
#the start position on the grid for the shapes 
#starts at the first (index 0) list in the 2d list called grid
#and at spot 8 in that second list 
#also, I called these variables i,j becuase x and y were confusing due to
#"backwards" (counter-intuitive) structure of 2D lists
i,j= 1,8

#-----SHAPES-----#
shape1=[[1,1,0,0],
        [1,1,0,0]]
        
shape2=[[2,2,2,2],
        [0,0,0,0]]
        
shape3=[[3,3,0,0],
        [0,3,3,0]]

shape4=[[0,0,4,4],
        [0,4,4,0]]
        
shape5=[[5,0,0,0],
        [5,5,5,0]]

shape6=[[0,0,0,6],
        [0,6,6,6]]

shape7=[[0,7,0,0],
        [7,7,7,0]]
#list of all tetris shapes: 
shapes=[shape1,shape2,shape3,shape4,shape5,shape6,shape7]

#-----FUNCTIONS-----#

def drawGrid(grid):
    'Draws the grid on screen'
    x,y=75,50
    boxsize=30
    for row in grid:
        for col in row:
            box=Rect(x,y,boxsize,boxsize)
            draw.rect(screen,(255,0,0),box,4)
            draw.rect(screen,(179,238,251),box)
            x+=boxsize
        y+=boxsize
        x=75

def rotate(shape):
    '''Rotates the shape
    This exact line of code is a very pythonic way to rotate matricies and was taken from:
    https://a.wordpress.com/2014/08/28/python-rotate-2d-arraymatrix-90-degrees-one-liner/''' 
    shape=list(zip(*shape[::-1]))     
    return shape
            
def addShape(shapes,grid,x,y):   
    'Adds shape to 2d grid by replacing blank spot with a number'
    try: 
        for i in range(len(shapes[0])):
            for j in range(len(shapes)):
                if shapes[j][i]!=0:
                    grid[x+i][y+j]=shapes[j][i]
    except IndexError:
        print ('erorr index')
        
def drawShape(grid,b):          
    'Draws shape that has landed on the grid. the b parameter is an image of a block'
    b=blocks() #list of the image of the individual blocks
    for i in range(20):
        for j in range(16):
            if grid[i][j]!=0:
                screen.blit(b[grid[i][j]],(15+j*30,20+i*30))
                
def drawFallShape(shapes,x,y,block):
    for i in range(len(shapes)):
            for j in range(len(shapes[0])):
                if shapes[i][j]!=0:
                    if x+i>=0:
                        screen.blit(block,((15+y*30)+30*j,(20+x*30)+30*i))
                
def newShape(shapes):
    'Returns the next shape that will fall'
    shape=randint(0,len(shapes)-1)
    i,j=0,8 #makes new shape go back to original postion
    return shapes[shape]

def checkRowfill(grid,y): #works with removerowfill function below. 
    'Returns True if a row is filled' 
    for x in range(len(grid[0])):
        if grid[y][x]==0:
            return False
    return True

def removeRowFill(grid):
    'Removes the full row and moves above things down'
    y=len(grid)-1 #starting from the last row and moving upwards. There are 20 rows (from 0 to 19).
    fullrow=0
    while y>=0:
        if checkRowFill(grid,y):
            for i in range(y,0,-1): #going backwards 
                for x in range(len(grid[0])):
                    grid[i][x]=grid[i-1][x]
            for x in range(len(grid[0])):
            #for every other row except row 0, the prevois row matters in that
            #if there was a block there, then it would move down
            #but, for row 0, there is now previous row so that entire row
            #is blank, i.e. it has no blocks on it: 
                grid[0][x]=0
            fullrow+=1
        else:
            y-=1
    return fullrow
    
def collide(shape,direction,grid,x,y): ##change directions 
    'Returns True if collision occurs in any direction with the shape'
    for i in range(len(shape)): #y-axis 
            for j in range(len(shape[0])): #x-axis 
                if shape[i][j]!=0:
                    if direction=='left':
                        if grid[x+i][y+j-1]!=0:
                            return True
                    elif direction=='right':
                        if grid[x+i][y+j+1]!=0:
                            return True
                    elif direction=='down':
                        if grid[x+i+1][y+j]!=0:
                            return True
    return False

def rotateCheck(grid,shape,i,j):
    'Checks if a rotating is possible. True if collosiion, false if none' 
    for y in range(len(shape)):
        for x in range(len(shape[0])):
            if shape[i][j]!=0:
                if j+y>19: #checks if peice is at bottm and retunrs ture (i.e no collision)
                    return True
                if x+i>9: #change number
                    if not collide(grid,shape,'left',i,j):
                        i-=1
                        return False
                    else:
                        return True
                if x+i<0:
                    if not collide(grid,shape,'right',i,j):
                        y+=1
                        return False
                    else:
                        return True
                if grid[x+i][y+j]!=0:
                    return True
    return False

##def onBoard(shape,x,y):
##    '''Returns true if the x,y coordiates of the shape is not less
##    than the height of the board and not less than the width of the board'
##    and also not greater than the board. This means it's one the board. False
##    is returned otherwise'''
##    for i in range(len(shape)): #y-axis 
##        for j in range(len(shape[0])): #x-axis
##            if j+x>=0 and j+x<15 and y+i<19:
##                return True
##    return False

##def validPos(board,shape,x,y,direction):
##    'Returns True if the shape is on board' 
##    for i in range(len(shape)): #y -axis 
##        for j in range(len(shape[0])): #x-axis 
##            if direction=='left':
##                if j+x>2 and j+x<16 and i+y-1<20: #j+x>0 
##                    return True 
##            elif direction=='right':
##                if j+x+1>0 and j+x+1<16 and i+y<20:
##                    return True
##            elif direction=='down':
##                if j+x>0 and j+x<16 and i+y+1<20:
##                    return True
##    return False

def validPos(board,shape,x,y,direction):
    'Returns True if the shape is on board' 
    for i in range(len(shape)): #y -axis 
        for j in range(len(shape[0])): #x-axis 
            if direction=='left':
                if j+x+-1>0 and j+x+-1<16 and i+y<20:
                    return True 
            elif direction=='right':
                if j+x+1>0 and j+x+1<16 and i+y<20:
                    return True
            elif direction=='down':
                if j+x>0 and j+x<16 and i+y+1<20:
                    return True
    return False

def checkEndGame(grid):
    '''Checks if no more peices can fall which means game is over.
    Returns True if game is over, False if not. '''
    if grid[0][6]!=0 or grid[0][7]!=0 or grid[0][8]!=0 or grid[0][9]!=0: #change 0s to 1.
        return True
    return False 
def newGame(grid,level,score):
    'If game is over, reset everything'
    grid=[[0 for i in range(16)] for j in range(20)]
    level=0
    score=0
    i,j=0,8
    
##def shapesImg():
##    'Loading the shapes that will be displayed'
##    shape1=transform.scale(image.load('shape1.png'),(70,70))
##    shape2=transform.scale(image.load('shape2.png'),(70,70))
##    shape3=transform.scale(image.load('shape3.png'),(70,70))
##    shape4=transform.scale(image.load('shape4.png'),(70,70))
##    shape5=transform.scale(image.load('shape5.png'),(70,70))
##    shape6=transform.scale(image.load('shape6.png'),(70,70))
##    shape7=transform.scale(image.load('shape7.png'),(70,70))
##    return [shape1,shape2,shape3,shape4,shape5,shape6]
    
def blocks():
    'Loading the individual blocks that make up a piece'
    b1=transform.scale(image.load('b1.png'),(30,30))
    b2=transform.scale(image.load('b2.png'),(30,30))
    b3=transform.scale(image.load('b3.png'),(30,30))
    b4=transform.scale(image.load('b4.png'),(30,30))
    b5=transform.scale(image.load('b5.png'),(30,30))
    b6=transform.scale(image.load('b6.png'),(30,30))
    b7=transform.scale(image.load('b7.png'),(30,30))
    return [b1,b2,b3,b4,b5,b6,b7]

def game():
    global grid,shapes,i,j

    
    myClock= time.Clock()
    arialFont=font.SysFont('Arial',20)
    
    gameState=True
    
    level=1
    score=0

    nextShape=newShape(shapes)
    shape=newShape(shapes)
    
    b=blocks()
    num=randint(0,len(b)-1)
    block=b[num]

    drawGrid(grid)
 
    running=True
    while running:
        for e in event.get():
            if e.type==QUIT:
                running=False
            if e.type==KEYDOWN:
                if e.key==K_UP:
                    if rotateCheck(grid,shape,i,j):
                        shape=rotate(shape)
                if e.key==K_SPACE:
                    pauseScreen(screen,mx,my,mb)
                    
        shape=nextShape
        nextShape=newShape(shapes) 

        mx,my=mouse.get_pos()
        mb=mouse.get_pressed() 
        keys= key.get_pressed()

        if keys[K_LEFT]:
            if validPos(grid,shapes[0],i,j,'left'):
                j-=1
        elif keys[K_RIGHT]:
            if validPos(grid,shapes[0],i,j,'right'):
                j+=1
        elif keys[K_DOWN]:
            if validPos(grid,shapes[0],i,j,'down'):
                i+=1
##        elif keys[K_UP]:
##            shape=rotate(shape)
                
        if checkEndGame(grid):
            gameState=False
        if not gameState:
            gameOver(arialFont,screen,mx,my,mb)
        if gameState:
            playMusic()
            
        removeRowFill(grid)
        score+=removeRowFill(grid) * 5
        level=getLevel(score)
        displayLevel(level,arialFont)
        displayScore(score,arialFont)
        drawFallShape(shape,i,j,block)
        addShape(shape,grid,i,j)
        display.flip()
        myClock.tick(24) 
    #move the shape by checking collision etc.
    #creae shape variable store shape
    #control the falling of the shape with speed
    #control the rotation of the peice 
    #make peice fall faster if key is held
    #then draw everything 

#-----------------------------------------------------------------------# 
running=True

shape=newShape(shapes)     #when game first starts
nextShape=newShape(shapes) #when game first starts

b=blocks()
num=randint(0,len(b)-1)
block=b[num]

drawGrid(grid)
myClock=time.Clock()
while running:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==K_UP:
            shape=rotate(shape)

    keys=key.get_pressed()
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    
    direction=''
        
    if keys[K_LEFT]:
        if validPos(grid,shape,i,j,'left'):                 
            j-=1
            direction='left'
    elif keys[K_DOWN]:
        if validPos(grid,shape,i,j,'down'):                     
            i+=1 
            direction='down'
    elif keys[K_RIGHT]:
        if validPos(grid,shape,i,j,'right'):
            j+=1
            direction='right'
##    if direction=='right' or direction=='left' or direction=='down':
##        if j>0 and j<20:
##            j-=1
##            i+=1
            
##    elif keys[K_UP]:
##        shape=rotate(shape)




    drawFallShape(shape,i,j,block)
    addShape(shape,grid,i,j)
    
                         
    myClock.tick(24)           
            
    #--------------------
    display.flip()
pprint(grid)
quit()
