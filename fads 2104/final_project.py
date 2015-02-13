# Sandeep Yalamanchili
# FADS final Project


import nltk
from nltk import word_tokenize
from nltk.util import ngrams

def make_grams(tokens,num):
    return ngrams(tokens,num)

def stop_test(word):
    global stopwords
    if word not in stopwords:
        return 1
    else:
        return 0


def main():
    text = "where f is a function that operates on a hello world word to compute its complete object testing"

    print(text)

    global stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    print(stopwords)


    token = nltk.word_tokenize(text)

    bigrams = ngrams(token,2)
    trigrams = ngrams(token,3)

    '''
    bigrams = make_grams(token,2)
    trigrams = make_grams(token,3)
    '''

    print(type(bigrams))
    print(trigrams)

    for gram in bigrams:
        #if(gram[0].lower() not in stopwords and gram[1].lower() not in stopwords):
         #   print(gram)
         if(stop_test(gram[0].lower()) and stop_test(gram[1].lower())):
             print(gram)


    for gram in trigrams:
        if(stop_test(gram[0].lower()) and stop_test(gram[1].lower()) and stop_test(gram[2].lower())):
            print(gram)        


main()
