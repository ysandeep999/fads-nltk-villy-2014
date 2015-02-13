import nltk
from nltk.corpus import brown

def main():
    word_sum = 0
    sent_sum = 0
    for word in nltk.corpus.brown.words():
        word_sum += len(word)

    um = word_sum / len(nltk.corpus.brown.words())

    print(um)



main()
