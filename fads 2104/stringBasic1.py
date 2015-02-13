def main():

    s1 = "spam"
    s2 = "ni!"

    print(s2.upper())
    
    print(s2 + s1 + s2)
    
    print((s1.capitalize().ljust(5) + s2.capitalize()).ljust(10) * 3)
    
    print(s1.lower())

    strlst = s1.split("a")
    print(strlst)


    listconcat = ""
    for i in strlst:
        listconcat = listconcat + i
    print(listconcat)

    input("\n\n press enter to exit: ")


    
main()
