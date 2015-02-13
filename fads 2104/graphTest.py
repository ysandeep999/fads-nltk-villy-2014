from graphics import *
def main():
    win = GraphWin("drawing",900,500)
    p =    Point(138,50)
    p.draw(win)
    
    circ = Circle(p,50)
    circ.draw(win)
    
    rect = Rectangle(Point(30,240),Point(70,108))
    rect.draw(win)

    line = Line(Point(0,0),Point(900,900))
    line.draw(win)

    text = Text(Point(234,134),"hehe")
    text.draw(win)

    oval = Oval(Point(23,45),Point(45,87))
    oval.draw(win)

main()
