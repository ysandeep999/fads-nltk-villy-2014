from graphics import *

def face(p,s,win):
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
    



def main():

    win = GraphWin("Face",500,500)
    p1 = Point(250,250)
    size = 50

    face(p1,size,win)

main()
