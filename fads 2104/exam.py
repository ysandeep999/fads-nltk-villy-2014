import nltk
from nltk.book import *


def main():
    sent1 = nltk.sents(text4)
    sent2 = nltk.sents(text5)
    print(sent1 * 3, sent2 * 3)
    print(sent1[:5],sent2[:5])
    
main()
