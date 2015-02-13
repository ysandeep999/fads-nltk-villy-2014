def main():

    for ch in "aardvark":
        print(ch)
    print()

    for w in "Now is the winter of our discontent...".split():
        print(w)

    print()

    for w in "Mississippi".split("i"):
        print(w, end=" ")
        
    print("\n")

    msg = ""
    for s in "secret".split("e"):
        msg = msg + s
    print(msg)

    print()
    
    msg = ""
    for ch in "secret":
        msg = msg + chr(ord(ch)+1)
    print(msg)

    input("\n press enter to exit :")
        

main()
