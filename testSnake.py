#---IMPORTS---#
from pygame import *
import pygame as pygame #for font to work 
from tkinter import *
from math import hypot
from random import randint
from os import environ
#---TK SETUP (for message box, saving and loading)---#
root= Tk() #initializing Tkinter engine
root.withdraw() #hides the window that pops up
#---FONT SETUP---#
pygame.font.init()
comicFont=pygame.font.SysFont("Comic Sans MS",16)
def getText(screen,x,y,fontname,col,size): #function for text tool. Allows user to type text on canvas
    ans = ""                    # final answer will be built one letter at a time.
    back = screen.subsurface(canvasRect).copy()        # copy screen so it can be replaced text is typed
    #---cursor---#
    textArea = Rect(x,y,1,1) #for cursorShow purposes 
    cursorShow = 0 
    myclock = time.Clock()
    #------------#
    typing = True
    while typing:
        cursorShow += 1
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN :
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans        
        #---cursor---#
        txtPic = fontname.render(ans, True, col)
        screen.blit(txtPic,(x,y))
        if cursorShow // 50 % 2 == 1:
            cx = textArea.x+txtPic.get_width()+3
            cy = textArea.y+3
            draw.rect(screen,col,(cx,cy,2,size)) #vertical line that appers after each chracter that is typed
        myclock.tick(100) #makes the vertical line above appear then disapear, repeatedly.
        #------------#
        display.flip()
        screen.subsurface(canvasRect).blit(back,(0,0))
    return ans #returns what the user typed

def hover(rect,sp,ep):       #this function is written because this block of code is written multiple times in the program and has no meaning except that it
    if rect.collidepoint(mx,my):  #makes the icon a diffrent color when hovering over it. So instead of writing the code in multiple lines,
        draw.rect(screen,(0,0,255),rect,2) #I wrote a function to just write it in one line to make code appear neater..
#---SCREEN SETUP---#
init()
inf = display.Info()
cen=(inf.current_w-1200)/2 #finds the x coordinate so that the screen can be centered (this is how much distance there'll be from the left and right corner of computer screen to the left and right corner (respectively)of the paint program screen)
environ['SDL_VIDEO_WINDOW_POS'] = '%d,25'%cen 
screen=display.set_mode((1200,700))
display.set_caption('Untitled-Pacman PaintBook')
display.set_icon(image.load('images/logo.jpg'))
#---FLAGS and other VARIABLES---#
tools='Pencil' #stores which tool is selected. Default tool is pencil so when you open the program, pencil will be selected
text='' #stores the text options (bold, underline, italics, etc.)
play='on' #for the play and pause option
info='' #stores the instruction for each tool

boldOnOff=0 #falg where 1 is added onto if bold is clicked
italicOnOff=0 #flag where 1 is added onto if italics is clicked
bold=False #if boldOnOff is an odd number, it means bold is clicked therefore bold will be true. Otherwise False. boldOnOff starts out as even so bold is false.
italic=False #if italicOnOff is an odd number, it means italics is clicked therefore italic will be true. Otherwise false. italicOnOff starts out as even so italic is false.



size=10 #size for stickers,shapes,text and all the tools execpt pencil
c=(0,0,0) #the defualt color is black for all drawing tools (except eraser),text tools and shape options. 

mx,my= 0,0
#---LOADING/RESIZING IMAGES and RECTs FOR ICONS---#
#BACKGROUND (two images were blitted so that the background doesn't look stretched and pixalated)
screen.blit(image.load('images/pacman.jpg').convert_alpha(),(0,0)) #convert_alpha makes the image load faster
screen.blit(image.load('images/pacman.jpg').convert_alpha(),(817,0))
#CANVAS
canvasRect= Rect(350,70,795,610)
draw.rect(screen,(255,255,255),canvasRect) #white canvas
draw.rect(screen,(0,0,255),(346,66,801,617),5) #border for canvas
#-SUBTITLEBAR IMAGES and RECTs-#
draw.rect(screen,(60,60,60),(0,0,1200,50)) #background for subtitle bar
draw.rect(screen,(0,0,255),(0,2,1199,49),3) #border for background for subtitle bar 
#UNDO pic/rect
undoRect= Rect(13,5,40,40)
n_undoPic=transform.scale(image.load('images/normal/n_undo.png'),(40,40)) 
#REDO pic/rect
redoRect= Rect(68,5,40,40)
n_redoPic=transform.scale(image.load('images/normal/n_redo.png'),(40,40)) 
#SAVE pic/rect 
saveRect= Rect(1092,5,40,40)
n_savePic=transform.scale(image.load('images/normal/n_save.png'),(40,40))
#LOAD pic/rect 
loadRect= Rect(1147,5,40,40)
n_loadPic=transform.scale(image.load('images/normal/n_open.png'),(40,40))
#COLOR SPECTRUM pic/rect
colorspecRect= Rect(75,370,215,325)
screen.blit(transform.scale(image.load('images/colorspectrum.png'),(215,325)),(75,370))
draw.rect(screen,(0,0,255),(72,367,220,329),3) #border for colorspectrum 
#COLOR PREVIEW rect
colorboxRect= Rect(1037,5,40,40) 
draw.rect(screen,c,colorboxRect) #box where color chosen is displayed
#-SIDE BAR IMAGES and RECTs-#
draw.rect(screen,(60,60,60),(0,60,66,640)) #background for display of tools
draw.rect(screen,(0,0,255),(0,58,66,640),3) #border for background for display of tools
#TAB for all tools 
tab= Rect(75,61,215,292) 
draw.rect(screen,(0,0,255),(72,59,220,297),3) #border for tab
#PENCIL pic/rect
pencilRect= Rect(13,65,40,40)
n_pencil=transform.scale(image.load('images/normal/n_pencil.png'),(40,40)) #normal image of icon
c_pencil=transform.scale(image.load('images/click/c_pencil.png'),(40,40)) #clicked image of icon 
#ERASER pic/rect
eraserRect= Rect(13,110,40,40)
n_eraserPic=transform.scale(image.load('images/normal/n_eraser.png'),(40,40)) #normal
c_eraserPic=transform.scale(image.load('images/click/c_eraser.png'),(40,40)) #click
#MARKER pic/rect
markerRect= Rect(13,155,40,40)
n_markerPic=transform.scale(image.load('images/normal/n_marker.png'),(40,40)) #normal
c_markerPic=transform.scale(image.load('images/click/c_marker.png'),(40,40)) #click
#PAINTBRUSH pic/rect
paintbrushRect= Rect(13,200,40,40)
n_paintbrushPic=transform.scale(image.load('images/normal/n_paintbrush.png'),(40,40)) #normal
c_paintbrushPic=transform.scale(image.load('images/click/c_paintbrush.png'),(40,40)) #click
#SPRAY PAINT pic/rect
sprayRect= Rect(13,245,40,40)
n_sprayPic=transform.scale(image.load('images/normal/n_spray.png'),(40,40)) #normal
c_sprayPic=transform.scale(image.load('images/click/c_spray.png'),(40,40)) #click 
#STICKERS pic/rect
stickersRect= Rect(13,290,40,40)
n_stickersPic=transform.scale(image.load('images/normal/n_sticker.png'),(40,40)) #normal
c_stickersPic=transform.scale(image.load('images/click/c_sticker.png'),(40,40)) #click
#ghost1 (sticker)
ghost1Rect= Rect(95,65,50,50)
ghost1=transform.scale(image.load('images/ghost1.png'),(50,50)) #this image has a transparent background and is the image blitted onto canvas if this sticker is selected
n_ghost1=transform.scale(image.load('images/normal/n_ghost1.png'),(50,50)) #normal
c_ghost1=transform.scale(image.load('images/click/c_ghost1.png'),(50,50)) #click
#ghost2 (sticker)
ghost2Rect= Rect(220,65,50,50)
ghost2=transform.scale(image.load('images/ghost2.png'),(50,50)) #transparent background
n_ghost2=transform.scale(image.load('images/normal/n_ghost2.png'),(50,50)) #normal
c_ghost2=transform.scale(image.load('images/click/c_ghost2.png'),(50,50)) #click
#ghost3 (sticker)
ghost3Rect= Rect(95,125,50,50)
ghost3=transform.scale(image.load('images/ghost3.png'),(50,50)) #transparent background
n_ghost3=transform.scale(image.load('images/normal/n_ghost3.png'),(50,50)) #normal
c_ghost3=transform.scale(image.load('images/click/c_ghost3.png'),(50,50)) #click
#ghost4 (sticker)
ghost4Rect= Rect(220,125,50,50)
ghost4=transform.scale(image.load('images/ghost4.png'),(50,50)) #transparent background
n_ghost4=transform.scale(image.load('images/normal/n_ghost4.png'),(50,50)) #normal
c_ghost4=transform.scale(image.load('images/click/c_ghost4.png'),(50,50)) #click
#cherry (sticker)
cherryRect= Rect(95,185,50,50)
cherry=transform.scale(image.load('images/cherry.png'),(50,50)) #transparent background
n_cherry=transform.scale(image.load('images/normal/n_cherry.png'),(50,50)) #normal
c_cherry=transform.scale(image.load('images/click/c_cherry.png'),(50,50)) #click
#strawberry (sticker)
strawberryRect= Rect(220,185,50,50) 
strawberry=transform.scale(image.load('images/strawberry.png'),(50,50)) #transparent background
n_strawberry=transform.scale(image.load('images/normal/n_strawberry.png'),(50,50)) #normal
c_strawberry=transform.scale(image.load('images/click/c_strawberry.png'),(50,50)) #click
#pacman1 (sticker)
pacman1Rect= Rect(95,245,50,50)
pacman1=transform.scale(image.load('images/pacman1.png'),(50,50)) #transparent background
n_pacman1=transform.scale(image.load('images/normal/n_pacman1.png'),(50,50)) #normal
c_pacman1=transform.scale(image.load('images/click/c_pacman1.jpg'),(50,50)) #click
#pacman2 (sticker)
pacman2Rect= Rect(220,245,50,50)
pacman2=transform.scale(image.load('images/pacman2.png'),(50,50))#transparent background
n_pacman2=transform.scale(image.load('images/normal/n_pacman2.png'),(50,50)) #normal
c_pacman2=transform.scale(image.load('images/click/c_pacman2.png'),(50,50)) #click
#SHAPES pic/rect
shapesRect= Rect(13,335,40,40)
n_shapesPic=transform.scale(image.load('images/normal/n_shapes.png'),(40,40)) #normal
c_shapesPic=transform.scale(image.load('images/click/c_shapes.png'),(40,40)) #click
shapestab= Rect(1075,50,155,400)
#rectangle unfilled
rectRect= Rect(95,65,50,50)
n_rectPic=transform.scale(image.load('images/normal/n_rect.png'),(50,50)) #normal
c_rectPic=transform.scale(image.load('images/click/c_rect.png'),(50,50)) #click
#rectangle filled
rectfRect= Rect(220,65,50,50)
n_rectfPic= transform.scale(image.load('images/normal/n_rectf.png'),(50,50)) #normal
c_rectfPic= transform.scale(image.load('images/click/c_rectf.png'),(50,50))#click
#ellipse unfilled
elRect= Rect(95,125,50,50)
n_elPic=transform.scale(image.load('images/normal/n_circle.png'),(50,50)) #normal
c_elPic=transform.scale(image.load('images/click/c_circle.png'),(50,50)) #click
#ellipse filled
elfRect= Rect(220,125,50,50) 
n_elfPic=transform.scale(image.load('images/normal/n_circlef.png'),(50,50)) #normal
c_elfPic=transform.scale(image.load('images/click/c_circlef.png'),(50,50)) #click
#polygon unfilled
polyRect= Rect(95,185,50,50)
n_polyPic=transform.scale(image.load('images/normal/n_polygon.png'),(50,50)) #normal
c_polyPic=transform.scale(image.load('images/click/c_polygon.png'),(50,50)) #click
#polygon filled
polyfRect= Rect(220,185,50,50)
n_polyfPic=transform.scale(image.load('images/normal/n_polygonf.png'),(50,50)) #normal
c_polyfPic=transform.scale(image.load('images/click/c_polygonf.png'),(50,50)) #click
#line
lineRect= Rect(95,245,50,50)
n_linePic=transform.scale(image.load('images/normal/n_line.png'),(50,50)) #normal
c_linePic=transform.scale(image.load('images/click/c_line.png'),(50,50)) #click
#TEXT
textRect= Rect(13,380,40,40)
n_textPic= transform.scale(image.load('images/normal/n_text.png'),(40,40)) #normal
c_textPic= transform.scale(image.load('images/click/c_text.png'),(40,40)) #click
#bold
boldRect= Rect(95,65,50,50)
n_boldPic=transform.scale(image.load('images/normal/n_bold.png'),(50,50)) #normal
c_boldPic=transform.scale(image.load('images/click/c_bold.png'),(50,50)) #click
#italic
italicRect= Rect(220,65,50,50)
n_italicPic=transform.scale(image.load('images/normal/n_italic.png'),(50,50)) #normal
c_italicPic=transform.scale(image.load('images/click/c_italic.png'),(50,50)) #click
#SELECT pic/rect (for copy, paste and cut)
selectRect= Rect(13,425,40,40)
n_selectPic=transform.scale(image.load('images/normal/n_sel.png'),(40,40)) #normal
c_selectPic=transform.scale(image.load('images/click/c_sel.png'),(40,40)) #click
#copy
copyRect= Rect(95,65,50,50)
n_copyPic=transform.scale(image.load('images/normal/n_copy.png'),(50,50)) #normal
c_copyPic=transform.scale(image.load('images/click/c_copy.png'),(50,50)) #click
#paste
pasteRect= Rect(220,65,50,50)
n_pastePic=transform.scale(image.load('images/normal/n_paste.png'),(50,50)) #normal
c_pastePic=transform.scale(image.load('images/click/c_paste.png'),(50,50)) #click
#cut
cutRect= Rect(95,125,50,50)
n_cutPic=transform.scale(image.load('images/normal/n_cut.png'),(50,50)) #normal
c_cutPic=transform.scale(image.load('images/click/c_cut.png'),(50,50)) #click
#FILTER
filterRect= Rect(13,470,40,40)
n_filterPic=transform.scale(image.load('images/normal/n_filter.png'),(40,40)) #normal
c_filterPic=transform.scale(image.load('images/click/c_filter.png'),(40,40)) #click
#black and white filter
bandwRect= Rect(90,65,150,25)
#negative filter
negativeRect= Rect(90,95,150,25)
#COLOR FILL pic/rect
colorfRect= Rect(13,515,40,40)
n_colorfPic=transform.scale(image.load('images/normal/n_fillcolor.png'),(40,40)) #normal
c_colorfPic=transform.scale(image.load('images/click/c_fillcolor.png'),(40,40)) #click
#PLAY
n_playPic=transform.scale(image.load('images/normal/n_play.png'),(40,40)) #normal
#PAUSE
n_pausePic=transform.scale(image.load('images/normal/n_pause.png'),(40,40)) #normal
#PLAY/PAUSE rect
playpauseRect= Rect(13,560,40,40)
screen.blit(n_pausePic,(13,560)) #music starts off by playing so pause pic is displayed so if user clicks pause pic, then music pauses and icon changes to play.
#ROTATE
rotateRect= Rect(13,605,40,40)
n_rotatePic=transform.scale(image.load('images/normal/n_rotate.png'),(40,40)) #normal
c_rotatePic=transform.scale(image.load('images/click/c_rotate.png'),(40,40)) #click
#vertical flip
vflipRect= Rect(90,65,50,50)
n_vflipPic= transform.scale(image.load('images/normal/n_vertical.png'),(50,50)) #normal
#horozontial flip
hflipRect= Rect(220,65,50,50)
n_hflipPic= transform.scale(image.load('images/normal/n_horozontial.png'),(50,50)) #normal
#rotate clockwise
clockwiseRect= Rect(90,125,50,50)
n_clockwisePic= transform.scale(image.load('images/normal/n_270.png'),(50,50)) #normal
#rotate counter-clockwise
counterwiseRect= Rect(220,125,50,50)
n_counterwise= transform.scale(image.load('images/normal/n_90.png'),(50,50)) #normal
#TRASH
trashRect= Rect(13,650,40,40)
n_trashPic=transform.scale(image.load('images/normal/n_trash.png'),(40,40)) #normal
c_trashPic=transform.scale(image.load('images/click/c_trash.png'),(40,40)) #click
#---BACKGROUND MUSIC---# (placed here so that music starts playing after all images load)
init()
mixer.music.load('Pacman-Dubstep-Remix.wav')
mixer.music.play(-1)
#---UNDO and REDO LIST---#
undo=[screen.subsurface(canvasRect).copy()]
redo=[]

copy1= False
copy1Rect= Rect(0,0,0,0)
cut1Rect=  Rect(0,0,0,0)
#---EVENT LOOP---#
running=True
while running:
    click=False
    saveK=False
    loadK=False
    undoK=False
    redoK=False
    for e in event.get():
        if e.type==QUIT:
            quest=messagebox.askyesnocancel('Paint','Do you want to save your work?')
            if quest==None: #if cancel is clicked, None is returned 
                running=True
            elif quest==True: # if yes is clicked, True is returned
                save()
                running=False
            else: # otherwise user clicked no. 
                running=False
        if e.type== MOUSEBUTTONUP: #takes a screenshot of the canvas once the mouse is released somewhere on the canvas and appends it to the undo list.
                if canvasRect.collidepoint(mx,my) and e.button==1: #if mouse is clicked on the canvas and then released (so that nothing appends to undo when you scroll up or down)
                    undo.append(screen.subsurface(canvasRect).copy())
        if e.type == MOUSEBUTTONDOWN:
            if canvasRect.collidepoint(mx,my) and tools=='Stickers' or tools=='Shapes' or tools=='Select' or tools=='Rotate': #a screenshot of the screen is taken if those tools are selected and if mouse is on canvas
                pic=screen.subsurface(canvasRect).copy()
            if e.button == 1:
               click=True
               sx,sy = e.pos
            if e.button == 4:
                if size!=90: #this ensures that the size will not exceed the maximum size (90)
                    size += 1
            if e.button == 5:
                if size>1: #this ensures that size doesn't become a negative number
                    size -= 1
        if e.type== KEYDOWN:
            if e.mod and KMOD_CTRL>0: # if user has clicked ctrl on the left or right
                if e.key== K_s:
                    saveK=True
                elif e.key==K_o:
                    loadK=True
                elif e.key== K_z:
                    undoK= True
                elif e.key== K_y:
                    redoK=True
    #----------------------------------------------------------#
    mb= mouse.get_pressed()
    omx,omy=mx,my
    mx,my= mouse.get_pos()
    #----------------------------------------------------------#
    #DISPLAYING INSTRUCTION FOR EACH TOOL (other than undo,redo,save and load)
    infoPic=comicFont.render(tools+': '+info,True,(0,0,255))
    draw.rect(screen,(234,234,234),(184,5,832,40)) #place where the info is displayed
    screen.blit(infoPic,(190,5))
    draw.line(screen,(128,128,128),(705,5),(705,40)) #vertical line in between info and mouse position (for design purposes)
    draw.line(screen,(128,128,128),(920,5),(920,40)) #vertical line in between mouse position and size (for design purposes)
    #DISPLAYING MOUSE POSITION
    if canvasRect.collidepoint(mx,my):
        mousePic = comicFont.render("Mouse Position: (%d,%d)"%(mx,my), True, (0,0,255))
        screen.blit(mousePic,(710,5))
    else:
        notoncanvas=comicFont.render("Mouse not on canvas",True,(0,0,255))
        screen.blit(notoncanvas,(710,5))
    #DISPLAYING SIZE OF TOOLS
    sizePic=comicFont.render("Size: %d"%size,True,(0,0,255))
    screen.blit(sizePic,(925,5))
    #DISPLAY INFORMATION FOR EACH TOOL ON THE TAB (not on the subtitle bar)
    if tools=='Eraser' or tools=='Marker' or tools=='Paintbrush' or tools=='Spray':
        toolPic=comicFont.render("Scroll to change size",True,(0,0,255)) #this is what is shows for the above tools on the tab
        draw.rect(screen,(234,234,234),tab) #draws a tab for each tool
        screen.blit(toolPic,(95,70))
    if tools=='Fill' or tools=='Play' or tools=='Pause' or tools=='Trash' or tools=='Colordrop' or tools=='Pencil': #for these tools, nothing is displayed on the tab
        draw.rect(screen,(234,234,234),tab) #the tab is blank for the above tools
    #when sticker, shapes, text, select, filter or rotate icons are clicked, the tab shows the different options for those tools. That part of the code is written below.
    #----------------------------------------------------------#
    #---Blitting the normal images for the icons---#
    screen.blit(n_undoPic,(13,5))
    screen.blit(n_redoPic,(68,5))
    screen.blit(n_colordropPic,(123,5))
    screen.blit(n_savePic,(1092,5))
    screen.blit(n_loadPic,(1147,5))
    screen.blit(n_pencil,(13,65))
    screen.blit(n_eraserPic,(13,110))
    screen.blit(n_markerPic,(13,155))
    screen.blit(n_paintbrushPic,(13,200))
    screen.blit(n_sprayPic,(13,245))
    screen.blit(n_stickersPic,(13,290))
    screen.blit(n_shapesPic,(13,335))
    screen.blit(n_textPic,(13,380))
    screen.blit(n_selectPic,(13,425))
    screen.blit(n_filterPic,(13,470))
    screen.blit(n_colorfPic,(13,515))
    screen.blit(n_rotatePic,(13,605))
    screen.blit(n_trashPic,(13,650))
    #---Blitting the hover images for the icons---#
    hover(undoRect,13,5)
    hover(redoRect,68,5)
    hover(colordropRect,123,5)
    hover(saveRect,1092,5)
    hover(loadRect,1147,5)
    hover(pencilRect,13,55)
    hover(eraserRect,13,110)
    hover(markerRect,13,155)
    hover(paintbrushRect,13,200)
    hover(sprayRect,13,245)
    hover(stickersRect,13,290)
    hover(shapesRect,13,335)
    hover(textRect,13,380)
    hover(selectRect,13,425)
    hover(filterRect,13,470)
    hover(colorfRect,13,515)
    hover(rotateRect,13,605)
    hover(trashRect,13,650)
    #---Blitting the clicked images for the icons---# 
    #PENCIL
    if mb[0]==1 and pencilRect.collidepoint(mx,my): tools='Pencil'
    if tools=='Pencil':
        screen.blit(c_pencil,(13,65))
        info='Click and drag on canvas to draw a thin line'
    #ERASER
    if mb[0]==1 and eraserRect.collidepoint(mx,my): tools='Eraser'
    if tools=='Eraser':
        screen.blit(c_eraserPic,(13,110))
        info='Click and drag on canvas to draw white cricles'
    #MARKER
    #had to be placed here for the size and color to change.
    marker = Surface((size,size),SRCALPHA) #blank surface
    draw.circle(marker,(c[0],c[1],c[2],10),(10,10),110) #draw using alpha
    if mb[0]==1 and markerRect.collidepoint(mx,my): tools='Marker'
    if tools=='Marker':
        screen.blit(c_markerPic,(13,155))
        info='Click and drag on canvas to draw a line with transperancy'
    #PAINTBRUSH
    if mb[0]==1 and paintbrushRect.collidepoint(mx,my): tools='Paintbrush'
    if tools=='Paintbrush':
        screen.blit(c_paintbrushPic,(13,200))
        info='Click and drag on canvas to draw colored circles'
    #SPRAY PAINT
    if mb[0]==1 and sprayRect.collidepoint(mx,my): tools='Spray'
    if tools=='Spray':
        screen.blit(c_sprayPic,(13,245))
        info='Click and drag on canvas to draw small random circles'
    #STICKERS
    if mb[0]==1 and stickersRect.collidepoint(mx,my):
        draw.rect(screen,(234,234,234),(tab))
        tools='Stickers'
    if tools=='Stickers': #if tools is stickers then the sticker options are placed on the tab
        screen.blit(c_stickersPic,(13,290))
        info='Select sticker and click on canvas to place'
        #---Blitting the normal images for sticker options---# 
        screen.blit(n_ghost1,(95,65))
        screen.blit(n_ghost2,(220,65))
        screen.blit(n_ghost3,(95,125))
        screen.blit(n_ghost4,(220,125))
        screen.blit(n_cherry,(95,185))
        screen.blit(n_strawberry,(220,185))
        screen.blit(n_pacman1,(95,245))
        screen.blit(n_pacman2,(220,245))
        #---Blitting the hover images for sticker options---#
        hover(ghost1Rect,95,65)
        hover(ghost2Rect,220,65)
        hover(ghost3Rect,95,125)
        hover(ghost4Rect,220,125)
        hover(cherryRect,95,185)
        hover(strawberryRect,220,185)
        hover(pacman1Rect,95,245)
        hover(pacman2Rect,220,245)
        #---Blitting the clicked images for sticker options---# (when user clicks on icon, it changes to the clicked image so it looks selected)
        #ghost1
        if mb[0]==1 and ghost1Rect.collidepoint(mx,my): stickers='ghost1'
        if stickers=='ghost1': screen.blit(c_ghost1,(95,65))
        #ghost2
        if mb[0]==1 and ghost2Rect.collidepoint(mx,my): stickers='ghost2'
        if stickers=='ghost2': screen.blit(c_ghost2,(220,65))
        #ghost3
        if mb[0]==1 and ghost3Rect.collidepoint(mx,my): stickers='ghost3'
        if stickers=='ghost3': screen.blit(c_ghost3,(95,125))
        #ghost4
        if mb[0]==1 and ghost4Rect.collidepoint(mx,my): stickers='ghost4'
        if stickers=='ghost4': screen.blit(c_ghost4,(220,125))
        #cherry
        if mb[0]==1 and cherryRect.collidepoint(mx,my): stickers='cherry'
        if stickers=='cherry': screen.blit(c_cherry,(95,185))
        #strawberry
        if mb[0]==1 and strawberryRect.collidepoint(mx,my): stickers='strawberry'
        if stickers=='strawberry': screen.blit(c_strawberry,(220,185))
        #pacman1
        if mb[0]==1 and pacman1Rect.collidepoint(mx,my): stickers='pacman1'
        if stickers=='pacman1': screen.blit(c_pacman1,(95,245))
        #pacman2
        if mb[0]==1 and pacman2Rect.collidepoint(mx,my): stickers='pacman2'
        if stickers=='pacman2': screen.blit(c_pacman2,(220,245))
    #SHAPES
    if mb[0]==1 and shapesRect.collidepoint(mx,my):
        draw.rect(screen,(234,234,234),(tab))
        tools='Shapes'
    if tools=='Shapes': #if shapes is slected then all the shape options are placed on the tab
        screen.blit(c_shapesPic,(13,335))
        info='Select shape and click and drag on canvas to place'
        #---Blitting the normal images for shape options---#
        screen.blit(n_rectPic,(95,65))
        screen.blit(n_rectfPic,(220,65))
        screen.blit(n_elPic,(95,125))
        screen.blit(n_elfPic,(220,125))
        screen.blit(n_polyPic,(95,185))
        screen.blit(n_polyfPic,(220,185))
        screen.blit(n_linePic,(95,245))
        #---Blitting the hover images for shape options---#
        hover(rectRect,95,65)
        hover(rectfRect,220,65)
        hover(elRect,95,125)
        hover(elfRect,220,125)
        hover(polyRect,95,185)
        hover(polyfRect,220,185)
        hover(lineRect,95,185)
        #---Blitting the clicked images for shape options---#
        #rectangle unfilled
        if mb[0]==1 and rectRect.collidepoint(mx,my): shapes='rect'
        if shapes=='rect': screen.blit(c_rectPic,(95,65))
        #rectangle filled
        if mb[0]==1 and rectfRect.collidepoint(mx,my): shapes='rectf'
        if shapes=='rectf': screen.blit(c_rectfPic,(220,65))
        #ellipse unfilled
        if mb[0]==1 and elRect.collidepoint(mx,my): shapes='ellipse'
        if shapes=='ellipse': screen.blit(c_elPic,(95,125))
        #ellipse filled
        if mb[0]==1 and elfRect.collidepoint(mx,my): shapes='ellipsef'
        if shapes=='ellipsef': screen.blit(c_elfPic,(220,125))
        #polygon unfilled
        if mb[0]==1 and polyRect.collidepoint(mx,my): shapes='poly'
        if shapes=='poly': screen.blit(c_polyPic,(95,185))
        #polygon filled
        if mb[0]==1 and polyfRect.collidepoint(mx,my): shapes='polyf'
        if shapes=='polyf': screen.blit(c_polyfPic,(220,185))
        #line
        if mb[0]==1 and lineRect.collidepoint(mx,my): shapes='line'
        if shapes=='line': screen.blit(c_linePic,(95,245))
        #instructions for polygon
        if shapes=='poly' or shapes=='polyf':
            rightclick=comicFont.render("Right click to create",True,(0,0,255))
            shape=comicFont.render("shape",True,(0,0,255))
            screen.blit(rightclick,(95,305))
            screen.blit(shape,(95,325))
        else:
            draw.rect(screen,(234,234,234),(95,305,190,45)) #if polygon is not selected, then show nothing at this place.
    #TEXT
    if mb[0]==1 and textRect.collidepoint(mx,my):
        draw.rect(screen,(234,234,234),(tab))
        tools='Text'
    if tools=='Text': #if text is selected, then the text options are places on the tab
        screen.blit(c_textPic,(13,380))
        info='Select text options and click on canvas to type text'
        screen.blit(comicFont.render('Click enter to stop',True,(0,0,255)),(240,22)) #blitted below the info for text if text is selected
        #---Blitting the normal images for text options---#
        screen.blit(n_boldPic,(95,65))
        screen.blit(n_italicPic,(220,65))
        #---Blitting the hover images for text options---#
        hover(boldRect,95,65)
        hover(italicRect,220,65)
        #---Blitting the clicked images for text options---#
        #bold
        if click and boldRect.collidepoint(mx,my): boldOnOff+=1
        if boldOnOff%2==1: bold=True  #if boldOnOff is an odd number, it means bold is clicked therefore bold will be true 
        else: bold=False              #otherwise False
        if bold==True: screen.blit(c_boldPic,(95,65)) #blitting the clicked image for bold, if it's been selected
        #italic
        if click and italicRect.collidepoint(mx,my): italicOnOff+=1
        if italicOnOff%2==1: italic=True #if italicOnOff is an odd number, it means italics is clicked therefore italic will be true 
        else: italic=False               #otherwise false
        if italic==True: screen.blit(c_italicPic,(220,65)) #blitting the clicked image for italics, if selected
    #SELECT
    if mb[0]==1 and selectRect.collidepoint(mx,my):
        draw.rect(screen,(234,234,234),tab)
        tools='Select'
    if tools=='Select':
        screen.blit(c_selectPic,(13,425))
        info='Choose to copy, paste or cut selected area on canvas'
        #---Blitting the normal images for select options---#
        screen.blit(n_copyPic,(95,65))
        screen.blit(n_pastePic,(220,65))
        screen.blit(n_cutPic,(95,125))
        #---Blitting the hover images for select options---#
        hover(copyRect,95,65)
        hover(pasteRect,220,65)
        hover(cutRect,95,125)
        #---Blitting the clicked images for select options---#
        #copy
        if mb[0]==1 and copyRect.collidepoint(mx,my): select='copy'
        if select=='copy': screen.blit(c_copyPic,(95,65))
        #paste
        if mb[0]==1 and pasteRect.collidepoint(mx,my): select='paste'
        if select=='paste': screen.blit(c_pastePic,(220,65))
        if mb[0]==1 and cutRect.collidepoint(mx,my): select='cut'
        if select=='cut': screen.blit(c_cutPic,(95,125))
    #FILTER
    if mb[0]==1 and filterRect.collidepoint(mx,my):
        tools='Filter'
        draw.rect(screen,(234,234,234),(tab))
    if tools=='Filter': #if filter is selected, then the filter options are placed on the tab 
        screen.blit(c_filterPic,(13,470))
        info='Click to add filter over canvas'
        #---Blitting the filter options---# 
        screen.blit(comicFont.render("Black and White",True,(0,0,255)),(95,65))
        draw.rect(screen,(255,0,0),bandwRect,2)
        screen.blit(comicFont.render("Negative",True,(0,0,255)),(95,95))
        draw.rect(screen,(255,0,0),negativeRect,2)
        #---Blitting the hover effect for filter options---#
        hover(bandwRect,95,65)
        hover(negativeRect,95,95)
        #---Using the filter---#
        if click and bandwRect.collidepoint(mx,my):
            for x in range(795): #there are 795 columns the in canvas
                for y in range(610): #there are 610 rows in the canvas
                #deals with all pixels of the canvas
                    r,g,b,a=screen.subsurface(canvasRect).get_at((x,y))
                    bw=int((r+g+b+a)/4) #finds the average of all the colors on the canvas to find the grey scale color
                    screen.subsurface(canvasRect).set_at((x,y),(bw,bw,bw,bw)) #makes the whole screen, the average of the r,g,b,a values
            undo.append(screen.subsurface(canvasRect).copy()) #adds a picture of the screen to undo list once filter is applied
            #placed here because when you use a filter, you don't release the mouse on the canvas which is when a screenshot of the canvas would normally be added to undo list
            #So, this had to be placed here for user to undo/redo filter effect 
        if click and negativeRect.collidepoint(mx,my):
            for x in range(795):
                for y in range(610):
                    r,g,b,a=screen.subsurface(canvasRect).get_at((x,y))
                    r,g,b,a=255-r,255-b,255-g,255 #inverts the colors to obtain a negative filter effect
                    screen.subsurface(canvasRect).set_at((x,y),(r,g,b,a))
            undo.append(screen.subsurface(canvasRect).copy()) #adds screenshot of screen to undo list once filter is applied
    #COLOR FILL
    if mb[0]==1 and colorfRect.collidepoint(mx,my): tools='Fill'
    if tools=='Fill':
        screen.blit(c_colorfPic,(13,515))
        info='Click on canvas to fill screen with color chosen'
    #PLAY/PAUSE
    #If you click on play, music plays and icon changes to pause. If you click pause, the music pauses and icon changes to play. 
    if click and playpauseRect.collidepoint(mx,my) and play=='on':
        screen.blit(n_playPic,(13,560))
        play='off'
        tools='Play'
        info='Click to play music'
        mixer.music.pause()
    elif click and playpauseRect.collidepoint(mx,my) and play=='off':
        screen.blit(n_pausePic,(13,560))
        play='on'
        tools='Pause'
        info='Click to pause music'
        mixer.music.unpause()
    #ROTATE
    if mb[0]==1 and rotateRect.collidepoint(mx,my):
        draw.rect(screen,(234,234,234),tab)
        tools='Rotate'
    if tools=='Rotate': #if rotate is selected, then the rotate options are placed on the tab
        screen.blit(c_rotatePic,(13,605))
        info='Select rotate options to rotate canvas'
        #---Blitting normal images---#
        screen.blit(n_vflipPic,(90,65))
        screen.blit(n_hflipPic,(220,65))
        screen.blit(n_clockwisePic,(90,125))
        screen.blit(n_counterwise,(220,125))
        #---Blitting hover image---#
        hover(vflipRect,90,65)
        hover(hflipRect,220,65)
        hover(clockwiseRect,90,125)
        hover(counterwiseRect,220,125)
        #---Using rotate options once you click it---#
        #vertical flip
        if vflipRect.collidepoint(mx,my) and click:
            canvasPic=transform.flip(pic,True,False)
            canvasPic=transform.scale(canvasPic,(795,610))
            screen.subsurface(canvasRect).blit(canvasPic,(0,0))
            undo.append(screen.subsurface(canvasRect).copy()) #the undo algorithim works in such way that if you release mouse on canvas, then it adds screenshot of canvas to list
            #when you use rotate options, that doesn't ocurr. Thus, I added a screenshot of the canvas when the user just clicks the rotate options. 
        #horozontial flip
        if hflipRect.collidepoint(mx,my) and click:
            canvasPic=transform.flip(pic,False,True)
            canvasPic=transform.scale(canvasPic,(795,610))
            screen.subsurface(canvasRect).blit(canvasPic,(0,0))
            undo.append(screen.subsurface(canvasRect).copy())
        #rotate clockwise
        if clockwiseRect.collidepoint(mx,my) and click:
            canvasPic=transform.rotate(pic,270)
            canvasPic=transform.scale(canvasPic,(795,610))
            screen.subsurface(canvasRect).blit(canvasPic,(0,0))
            undo.append(screen.subsurface(canvasRect).copy())
        #rotate counterclock wise
        if counterwiseRect.collidepoint(mx,my) and click:
            canvasPic=transform.rotate(pic,90)
            canvasPic=transform.scale(canvasPic,(795,610))
            screen.subsurface(canvasRect).blit(canvasPic,(0,0))
            undo.append(screen.subsurface(canvasRect).copy())
    #TRASH (if you click trash, the canvas is filled with white so that user can restart drawing)
    if click and trashRect.collidepoint(mx,my):
        tools='Trash'
        info='Click to restart drawing'
        screen.subsurface(canvasRect).fill((255,255,255))
        undo.append(screen.subsurface(canvasRect).copy()) 
    #UNDO (if you click undo, what you drew on the canvas is undid)
    if click and undoRect.collidepoint(mx,my) or undoK==True: undo_drawing()
    #REDO (if you click redo, what you drew on the canvas is redid)
    if click and redoRect.collidepoint(mx,my) or redoK==True: redo_drawing()
    #COLOR DROP (if you click this icon, then you click anywhere on the canvas, the color changes to the color on the canvas that you clicked at. Diplayed on preview box beside save button)
    if click and colordropRect.collidepoint(mx,my):
        tools='Colordrop'
        info='Choose color from canvas'
    #SAVE (if you cliik on save, then the canvas is saved)
    if click and saveRect.collidepoint(mx,my) or saveK==True: save()
    #LOAD (if you click on load, then the image file from your computer is loaded onto the canvas. The size of the image file changes to fit the canvas)
    if click and loadRect.collidepoint(mx,my) or loadK==True: load()
    #COLOR SPECTRUM (if you click on the color spectrum, the color changes to what you selected. This is displayed on the preview box beside the save button)
    if mb[0]==1 and colorspecRect.collidepoint(mx,my):
        c=screen.get_at((mx,my))
        draw.rect(screen,c,colorboxRect)
    #CONTROLS THE STICKER, SHAPE, TEXT and SELECT tools  
    if tools!='':
        if tools!='Stickers': #if the tools is not stickers then no sticker is selected so if you click on canvas, a sticker doesn't appear 
              stickers=''
        if tools!='Shapes': #if the tools is not shapes then set shape equal to blank. So, if you click on canvas, a shape doesn't appear
              shapes=''
        if tools!='Text': #if user is using any other tool then the text tool, then set text options equal to None so that if user clicks on canvas, text does not appear
              bold=None
              italic=None
        if tools!='Select': #if the tools is not select, then the select optiosn is set to blank so that if you click on canvas, select options (cut,copy,paste) doesn't occur.
              select=''
    #----------------------------------------------------------#
    #---USING THE TOOLS---#
    if canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect) #The user can only draw on the canvas
        if tools=='Pencil' and mb[0]==1:
            draw.aaline(screen,c,(omx,omy),(mx,my)) #aaline makes a smoother line
        elif (tools=='Eraser' or tools=='Marker' or tools=='Paintbrush') and mb[0]==1:
            dx,dy=mx-omx,my-omy  #delta x, delta y
            dist=hypot(dx,dy)
            #Draws circles at the x and y cordinates. Makes the tools smoother when you draw with it.
            for i in range(int(dist)):
                x,y=int(omx+i/dist*dx),int(omy+i/dist*dy)
                if tools=='Eraser':
                    draw.circle(screen,(255,255,255),(x,y),size) #draws white circles
                elif tools=='Marker': 
                    if mx!=omx or my!=omy:
                        screen.blit(marker, (x,y)) #draws colored rectangle with transperancy
                elif tools=='Paintbrush':
                    draw.circle(screen,c,(x,y),size) #draws colored circles
        elif tools=='Spray' and mb[0]==1:
            for i in range(int(size*2)): 
                x=randint(mx-size,mx+size) #takes random x coordinates within the rectangle
                y=randint(my-size,my+size) #takes random y coordinates within the rectangle
                if hypot(mx-x,my-y)<=size:
                    draw.line(screen,c,(x,y),(x,y))
        #stickers (if the user has slected one of the sticker options, and they have cliked on the canvas, the sticker is blitted where they clicked)
        elif stickers!='' and mb[0]==1:
            screen.subsurface(canvasRect).blit(pic,(0,0))
            if stickers=='ghost1':
                screen.blit(transform.scale(ghost1,(size,size)),(mx-10,my-10))
            elif stickers=='ghost2':
                screen.blit(transform.scale(ghost2,(size,size)),(mx-10,my-10))
            elif stickers=='ghost3':
                screen.blit(transform.scale(ghost3,(size,size)),(mx-10,my-10))
            elif stickers=='ghost4':
                screen.blit(transform.scale(ghost4,(size,size)),(mx-10,my-10))
            elif stickers=='cherry':
                screen.blit(transform.scale(cherry,(size,size)),(mx-10,my-10))
            elif stickers=='strawberry':
                screen.blit(transform.scale(strawberry,(size,size)),(mx-10,my-10))
            elif stickers=='pacman1':
                screen.blit(transform.scale(pacman1,(size,size)),(mx-10,my-10))
            elif stickers=='pacman2':
                screen.blit(transform.scale(pacman2,(size,size)),(mx-10,my-10))
        #shapes (if the user selects a shape option and then clicks on the canvas, the shape is drawn on the canvas where user clicked)
        elif (shapes=='rect' or shapes=='rectf') and mb[0]==1:
            screen.subsurface(canvasRect).blit(pic,(0,0))
            if shapes=='rect': #unfilled rectangle
                line=size//2#this how much more length is added on to the lines below to fix the weird edges.
                if mx>=sx: #drawing rectangle if you drag it towards the bottom right or top right from the start position(sx,sy).
                    draw.line(screen,c,(sx-line,sy),(mx+line,sy),size)
                    draw.line(screen,c,(mx,sy-line),(mx,my+line),size)
                    draw.line(screen,c,(mx+line,my),(sx-line,my),size)
                    draw.line(screen,c,(sx,my+line),(sx,sy-line),size)
                elif mx<=sx: #drawing rectangle if you drag it towards the bottom left or top left from the start position(sx,sy).
                    draw.line(screen,c,(sx+line,sy),(mx-line,sy),size)
                    draw.line(screen,c,(mx,sy+line),(mx,my-line),size)
                    draw.line(screen,c,(mx-line,my),(sx+line,my),size)
                    draw.line(screen,c,(sx,my-line),(sx,sy+line),size)
            elif shapes=='rectf': #filled rectangle
                drawRect= Rect(sx,sy,mx-sx,my-sy)
                drawRect.normalize()
                draw.rect(screen,c,drawRect)
        elif (shapes=='ellipse' or shapes=='ellipsef') and mb[0]==1:
            screen.subsurface(canvasRect).blit(pic,(0,0))
            if shapes=='ellipse': #unfilled ellipse
                #Checks if the width and height are greater then the diameter and draws ellipse. Otherwise, filled ellipse is drawn
                if abs(mx-sx)>size*2 and abs(my-sy)>size*2: 
                    drawel= Rect(min(sx,mx),min(sy,my),abs(mx-sx),abs(my-sy))
                    drawel.normalize()
                    draw.ellipse(screen,c,drawel,size)
                else: 
                    drawel= Rect(sx,sy,mx-sx,my-sy)
                    drawel.normalize()
                    draw.ellipse(screen,c,drawel)
            if shapes=='ellipsef': #filled ellipse
                drawelf= Rect(sx,sy,mx-sx,my-sy)
                drawelf.normalize()
                draw.ellipse(screen,c,drawelf)
        elif shapes=='poly' or shapes=='polyf':
            if click: #when user clicks on the canvas, the points they clicked at is added to the points list
                points.append((mx,my))
                if len(points)>1:
                    draw.line(screen,c,points[-2],points[-1],5) #a line is drawn connecting the points user clicked once there are two points in the points list
                else:
                    draw.circle(screen,c,(mx,my),5) #a circle is drawn when user first clicks canvas with polygon tool selected. Then once there are two points in the list, a linen is drwan
            if mb[2]==1:
                if len(points)>2:
                    if shapes=='poly':
                        draw.polygon(screen,c,points,5) #draws a polygon connecting all the points together with a thickness of 5 
                        del points[:]
                        undo.append(screen.subsurface(canvasRect).copy())
                    elif shapes=='polyf':
                        draw.polygon(screen,c,points) #draws a polygon connecting all the points together
                        del points[:]
                        undo.append(screen.subsurface(canvasRect).copy())
        elif shapes=='line' and mb[0]==1:
            screen.subsurface(canvasRect).blit(pic,(0,0))
            draw.line(screen,c,(sx,sy),(mx,my),size)
        #text (if user selects on the the text options then clicks the canvas, the text is displayed where they clicked with the option they selected on canvas)
        elif (bold==True and italic==True) and mb[0]==1: 
            arialFont=pygame.font.SysFont("Arial",size,bold=True,italic=True)
            textType=getText(screen,mx,my,arialFont,c,size)
            textPic=arialFont.render(textType,True,c)
            screen.blit(textPic,(mx,my))
            undo.append(screen.subsurface(canvasRect).copy()) # adds a picture of text you typed to the undo list so user can undo/redo text 
        elif (bold==False and italic==False) and mb[0]==1: 
            arialFont=pygame.font.SysFont("Arial",size)
            textType=getText(screen,mx,my,arialFont,c,size)
            textPic=arialFont.render(textType,True,c)
            screen.blit(textPic,(mx,my))
            undo.append(screen.subsurface(canvasRect).copy()) # adds the text you typed to the undo list so user can undo/redo text 
        elif bold==True and mb[0]==1: 
            arialFont=pygame.font.SysFont("Arial",size,bold=True,italic=False)
            textType=getText(screen,mx,my,arialFont,c,size)
            textPic=arialFont.render(textType,True,c)
            screen.blit(textPic,(mx,my))
            undo.append(screen.subsurface(canvasRect).copy()) # adds the text you typed to the undo list so user can undo/redo text 
        elif italic==True and mb[0]==1: 
            arialFont=pygame.font.SysFont("Arial",size,bold=False,italic=True)
            textType=getText(screen,mx,my,arialFont,c,size)
            textPic=arialFont.render(textType,True,c)
            screen.blit(textPic,(mx,my))
            undo.append(screen.subsurface(canvasRect).copy()) # adds the text you typed to the undo list so user can undo/redo text
        #select (if user clicks on one of the options(cut,copy,paste) then it cuts or copies area on canvas chosen by user and paste on place cliked by user on canvas))
        elif tools=='Select':
            if select=='copy':
                if mb[0]==1:
                    screen.subsurface(canvasRect).blit(pic,(0,0))
                    copy1Rect= Rect(sx,sy,mx-sx,my-sy)
                    copy1Rect.normalize()
                    draw.rect(screen,0,copy1Rect,3)
                if mb[0]==0:
                    draw.rect(screen,(255,255,255),copy1Rect,4)
                    copy1Pic=screen.subsurface(copy1Rect).copy()
            elif select=='paste' and mb[0]==1:
                screen.subsurface(canvasRect).blit(pic,(0,0))
                screen.blit(copy1Pic,(mx,my))
            elif select=='cut':
                if mb[0]==1:
                    screen.subsurface(canvasRect).blit(pic,(0,0))
                    cut1Rect=Rect(sx,sy,mx-sx,my-sy)
                    cut1Rect.normalize()
                    cut1Pic=screen.subsurface(cut1Rect).copy()
                    draw.rect(screen,0,cut1Rect,3)
                if mb[0]==0:
                    draw.rect(screen,(255,255,255),cut1Rect)
                if mb[2]==1:
                    screen.subsurface(canvasRect).blit(pic,(0,0))
                    screen.blit(cut1Pic,(mx,my))  
        elif tools=='Fill' and mb[0]==1:
            screen.subsurface(canvasRect).fill((c))
        elif tools=='Colordrop' and mb[0]==1:
            c=screen.get_at((mx,my)) 
        screen.set_clip(None)
        draw.rect(screen,c,colorboxRect) #this updates the color from colordrop to the color preview rectangle
    #----------------------------------------------------------
    display.flip()
pygame.font.quit()
quit()
