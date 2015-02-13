from graphics import *

def main():
    
    openfile = open("histo.txt", "r")
#    print("testing files", file = outfile)

    zero = 0
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0

    
    
    count = 0
    for line in openfile:
        count = count + 1
        if int(line) == 0:
            zero += 1
        if int(line) == 1:
            one += 1
        if int(line) == 2:
            two += 1
        if int(line) == 3:
            three += 1
        if int(line) == 4:
            four += 1
        if int(line) == 5:
            five += 1
        if int(line) == 6:
            six += 1
        if int(line) == 7:
            seven += 1

        if int(line) == 8:
            eight += 1
        if int(line) == 9:
            nine += 1

        if int(line) == 10:
            ten += 1
        

        
        '''
        if openfile.readline()== "0":
            zero = zero + 1
        if openfile.readline()== "1":
            one = one + 1
        if openfile.readline()== "2":
            two = two + 1
        if openfile.readline()== "3":
            three = three + 1
        if openfile.readline()== "4":
            four = four + 1
        if openfile.readline()== "5":
            five = five + 1
        if openfile.readline()== "6":
            siz = six + 1
        if openfile.readline()== "7":
            seven = seven + 1
        if openfile.readline()== "8":
            eight = eight + 1
        if openfile.readline()== "9":
            nine = nine + 1
        if openfile.readline()== "10":
            ten = ten + 1
        '''
    number = [zero,one,two,three,four,five,six,seven,eight,nine,ten]

    print("zero is :",zero)
    print("five is: ",five)
    print("six is: ",six)
    print(count)
    print(number)

    
    win = GraphWin("quix histogram",500,500)
    win.setCoords(0,0,20,20)
    
    for i in range(11):
        Text(Point(5.1+i,2.5),"{0}".format(i)).draw(win)
        Rectangle(Point(5+i,3),Point(5.3+i,3+number[i])).draw(win)

    
    

main()
