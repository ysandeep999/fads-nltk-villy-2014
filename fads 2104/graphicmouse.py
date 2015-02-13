from graphics import *

def main():
    win = GraphWin("mouse")
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1,p2,p3)
    triangle.draw(win)
#    triangle.setText("enter")

main()
