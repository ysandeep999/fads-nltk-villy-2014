#Sandeep Yalamanchili

import nltk,re

from nltk.corpus import conll2000



def grammer():
    grammar = r"""
              NP:
              {<.*>+}          # Chunk everything
              }<VBD|IN|>+{      # Chink sequences of VBD and IN
              """
    return grammar

def grammer1(item):
    grammar = r"""
              NP:
              {<.*>+}          # Chunk everything
              }<"""+item+""">+{      # Chink sequences of VBD and IN
              """
    return grammar

def grammer2(item,item1):
    grammar = r"""
              NP:
              {<.*>+}          
              }<"""+item+"|"+item1+""">+{
              """
    return grammar

def grammer3(item):
    grammar = r"""
              NP:
              {<.*>+}          # Chunk everything
              }<"""+item+""">+{      # Chink sequences of VBD and IN
              """
    return grammar



def main():
    
    lists = ["PRP","VBD","DT","JJ","NN","IN","NNP"]
    
    #for items in lists:
        
    
    cp = nltk.RegexpParser(grammer())
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
            #print(len(test_sents))
    print(cp.evaluate(test_sents))

main()
