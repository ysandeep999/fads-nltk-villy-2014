# Sandeep Yalamanchili
# There are 264 distinct words in the Brown Corpus having exactly three possibletags.

#Print a table with the integers 1..10 in one column, and the number of distinct
#words in the corpus having 1..10 distinct tags in the other column.
#For the word with the greatest number of distinct tags, print out sentences
#from the corpus containing the word, one for each possible tag.



import nltk
from nltk.corpus import brown

def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence): 
        if ( w2 == 'that' ):
            print(w1, w2, w3)


def sentences():

    print(".......................................")
    brown_tagged_sents = brown.tagged_sents(categories= 'news')
    print(len(brown_tagged_sents))
    print(type(brown_tagged_sents))
    set1 = list(brown_tagged_sents)
    set2 = set1
    print(len(set2))
    print(set2[2])
    print(set2[2][1])

    for incr in range(4623):
        leng = len(set2[incr])
        for incr2 in range(leng-1):
            if(set2[incr][incr2][0] == "that" and set2[incr][incr2][1] == "CS"):
                print("bon")
    if ("that","CS") in brown_tagged_sents:
        print("hola")
    lst = [(a,b) for (a,b) in set2 if a=="that" and b=="CS"]
        
    
    

def main():

    

    count = 0
    print([categ for categ in brown.categories()])
    #brown_tagged_sents = brown.tagged_sents(categories=[categ for categ in brown.categories()])
    #news_word = brown.words(categories='news')
    brown_news_tagged = brown.tagged_words(categories=[categ for categ in brown.categories()])

    
    data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)

    for word in sorted(data.conditions()):
        if len(data[word]) == 15 :
            ##print(word,data[word].most_common())
            lst = list(data[word].most_common())
            ##print(lst)
            #wrd_lst[count] = [b for [(a,b),(c,d),(e,f)] in data[word].most_common() and 3>1]
            
            ##if len(data[word].most_common()) == 3:
            tags = [tag for (tag, _) in data[word].most_common()]
    
            #if ((tags) == 3):]
            #if(len(tags) == 3):
            #print(tags)
                #for (_, 3) in data[word].most_common():
                #if data[word].most_common() == (tags,3):
            print(word, ' '.join(tags))
            count = count + 1
            #temp = ' '.join(tags)



    #brown_sents = brown.sents(categories='news')
    #unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
    #unigram_tagger.tag(brown_sents[2007])

    print(count)

    #for tagged_sent in brown.tagged_sents():
        #process(brown_tagged_sents)

main()

sentences()
