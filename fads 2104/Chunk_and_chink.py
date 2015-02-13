from nltk.corpus import conll2000
import nltk,re,pprint
from nltk import RegexpParser
def main():
    grammar = r"NP: {<.*><NNS>}"  
    grammar1 = r"""
    NP:
    {<.*>+}         
    }<VBD|IN>+{      
    """
    cp = nltk.RegexpParser(grammar1)      
    cp1 = nltk.RegexpParser(grammar)
    test_sents = conll2000.chunked_sents('test.txt')[:3]    
    print(cp.parse(test_sents))
    print("-----------")
    print(cp1.parse(test_sents))       
    print(cp.evaluate(test_sents))
    print(cp1.evaluate(test_sents))
main()
