# Sandeep Yalamanchili
#nltk_state-union-corpus.py
# Count occurrences in state union corpus
#Read in the texts of the State of the Union addresses, using the state_union
#corpus reader. Count occurrences of men, women, and people in each document.
#What has happened to the usage of these words over time?

import nltk
#from nltk.book import *
from nltk.corpus import state_union as su

def main():
#    print(len(su.fileids()))
#    all_word = ["men","women","people"]

    men_count = 0
    women_count = 0
    people_count = 0

    
    print(" men \t women \t people  \tfileid")
    print("-" * 50)

    for fileid in su.fileids():
        
        state = nltk.Text(su.words(fileid))
        men_count = state.count("men")
        women_count = state.count("women")
        people_count = state.count("people")
        print(men_count,"\t", women_count,"\t", people_count,"\t", fileid)

    input("press enter to exit: ")
        

 
    '''
    cfd = nltk.ConditionalFreqDist(
            (target,fileid[:])
            for fileid in su.fileids()
            for w in su.words(fileid)
            for target in ["men","women","people"]
            if w.startswith(target))
    cfd.plot()
    '''
    
#  fdist = FreqDist(w for set(for fileid in su.fileid()) and (w == allwords[0] or
#                                                            w == allwords[1] or
#                                                               w == allwords[2]))
    
#  fdist.dispersion.plot()
    
#    print((word for word in su and word == "men"))
main()

