# Sandeep Yalamanchili and Revathi allam
# Batch number 3
# drawing a smiley face on a GIF pic

from graphics import *
import os,sys
import math


def face(p,pr,win):
    s = math.sqrt(math.pow(p.getY() - pr.getY(),2) + math.pow(p.getX() - pr.getX(),2))
    circ = Circle(p,s)
    circ.setFill("yellow")
    circ.draw(win)
    

    p1 = Point(p.getX()-s//2, p.getY() - s//2)
    circ1 = Circle(p1, s//5)
    circ1.setFill("white")
    circ1.draw(win)

    p2 = Point(p.getX()+s//2, p.getY() - s//2)
    circ2 = Circle(p2, s//5)
    circ2.setFill("white")
    circ2.draw(win)

    p3 = Point(p.getX(), p.getY() + s//2)
    circ3 = Circle(p3, s//5)
    circ3.setFill("red")
    circ3.draw(win)


    p4 = Point(p.getX(), p3.getY() - s//5)
    circ4 = Circle(p4, s//5)
    circ4.setFill("yellow")
    circ4.setOutline("yellow")
    circ4.draw(win)
    
def funny(win,img):
    
    img.draw(win)
    p5 = win.getMouse()
    p5.draw(win)

    p6 = win.getMouse()
    p6.draw(win)
    face(p5,p6,win)
    


def main():

     
    win = GraphWin("Face",500,500)
    fname = "baby.gif"
    p1 = Point(250,250)
    img = Image(p1,fname)

    print("click on face center and face end to draw a smiley")
   
    funny(win,img)    
    
       

main()
