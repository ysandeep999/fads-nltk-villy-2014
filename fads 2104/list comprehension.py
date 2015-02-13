# Sandeep Yalamanchili
# list comprehension


def main():
    sent = ['The','dog','gave','John','the','newspaper']
    result = [(word,len(word)) for word in sent]
    print(result)

    input("\npress enter to exit")

main()



