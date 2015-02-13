# Sandeep Yalamanchili

import nltk,re,pprint
from nltk.corpus import conll2000
from nltk import RegexpParser


def grammer(sentence):
    grammar = r"NP: {<[CDJNP].*>+}"
    grammar1 = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(sentence)
    return result

def main():
        
    
        sen1 = conll2000.chunked_sents("train.txt",chunk_types='NP')[36]
        result = grammer(sen1)
        print(sen1)
        print(result)
        #print(result.draw())
        
    
main()
