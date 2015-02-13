# Sandeep Yalamanchili
# nltkbasic.py
#This program performs set of operations on the given list of words.

from nltk import *

def main():

    phrase = ["This","is","my","first","Nltk","program","."]
    phrase1 = ["Nltk","process","texts","in","python","language"]

    print("Addition operation on list: \n")
    print(phrase + phrase1)
    print("\n\n")

    print("Multiplication operation on list: \n")
    print(phrase * 3)
    print("\n\n")

    print("indexing operation on list: \n")
    print(phrase[4])
    print("\n\n")

    print("Slicing operation on list: \n")
    print(phrase[3:6])
    print("\n\n")

    print("Sorting operation on list: \n")
    print(sorted(w for w in phrase))
    print("\n\n")
    input("press enter to exit: ")
    

main()
