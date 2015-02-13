import nltk

from nltk.corpus import brown

def main(cat):
    word_sum = 0
    sent_sum = 0
    a = []
    for word in nltk.corpus.brown.words(categories = cat):
        word_sum += len(word)

    um = word_sum / len(nltk.corpus.brown.words(categories = cat))

    #print(um)

    for sent in nltk.corpus.brown.sents(categories = cat):
        #a = sent.split()
        sent_sum += len(sent)

    us = sent_sum / len(nltk.corpus.brown.sents(categories = cat))
    #print(us)
    return 4.71 * um + 0.5 * us - 21.43



def sec():

    categ = brown.categories()
    

    for cat in categ:        
        print(cat,"  ARI : ", main(cat))



sec()
        
