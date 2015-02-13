# Sandeep Yalamanchili
# unigram

import nltk
from nltk.corpus import brown

def main():
    

    #print(brown.categories())
    brown_tagged_sents = brown.tagged_sents(categories='news')
    brown_sents = brown.sents(categories='romance')
    unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
    print(unigram_tagger.tag(brown_sents[2000]))


main()
