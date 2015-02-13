# a prog for finding Acroynm

def main():
    sentence = input("enter a sentence : ")

    x = ""
#    print(("".join(word[0] for word in sentence.split(" "))).upper())

    for word in sentence.split(" "):
       x = x + "".join(word[0])

    print (x)

    

    




main()
