from graphics import *

def main():
    prin = eval(input("enter principal value: "))
    apr = eval(input("enter intrest: "))
    
    win = GraphWin("window",320,240)

    Text(Point(10,230),"     0.0K").draw(win)
    Text(Point(10,180),"    2.5K").draw(win)
    Text(Point(10,130),"    5.0K").draw(win)
    Text(Point(10,80),"    7.5K").draw(win)
    Text(Point(10,300),"   10.0K").draw(win)
#    Text(Point(319,240),"   test").draw(win)
    height = prin * 0.02
    rect = Rectangle(Point(40,230),Point(65,230-height))
    rect.draw(win)

    for i in range(10):
        prin = prin * (1 + apr)
        height = prin *0.02
        rect = Rectangle(Point(65 + 25 * i,230),Point(65+25*(i+1),230-height))
        rect.draw(win)
        
        

main()
