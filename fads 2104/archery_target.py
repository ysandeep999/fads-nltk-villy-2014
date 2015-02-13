from graphics import *

def main():
    win = GraphWin("Shoot it",500,500)

    radius = 20
    p = Point(250,250)
    

    circ5 = Circle(p,radius * 5)
    circ5.setFill("white")
    circ5.draw(win)

    circ4 = Circle(p,radius * 4)
    circ4.setFill("black")
    circ4.draw(win)

    circ3 = Circle(p,radius * 3)
    circ3.setFill("blue")
    circ3.draw(win)

    circ2 = Circle(p,radius * 2)
    circ2.setFill("red")
    circ2.draw(win)

    circ1 = Circle(p,radius * 1)
    circ1.setFill("yellow")
    circ1.draw(win)

    input(" Press enter to exit")
 
    

main()
