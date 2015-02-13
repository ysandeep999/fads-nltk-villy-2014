# Sandeep Yalamanchili

# a prog for finding Acroynm

def achroynm(phrase):
    #sentence = input("enter a sentence : ")

    x = ""
#    print(("".join(word[0] for word in sentence.split(" "))).upper())

    for word in phrase.split(" "):
       x = x + "".join(word[0])

    #print (x)

    return x

    





def main():

    sentence = 'Random Acess Memory'

    acr = achroynm(sentence)

    print(acr)

main()

    
