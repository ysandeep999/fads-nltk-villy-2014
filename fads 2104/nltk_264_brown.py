# Sandeep Yalamanchili
# There are 264 distinct words in the Brown Corpus having exactly three possibletags.

#Print a table with the integers 1..10 in one column, and the number of distinct
#words in the corpus having 1..10 distinct tags in the other column.
#For the word with the greatest number of distinct tags, print out sentences
#from the corpus containing the word, one for each possible tag.



import nltk
from nltk.corpus import brown

def main():

    count = 0
    print([categ for categ in brown.categories()])
    brown_news_tagged = brown.tagged_words(categories=[categ for categ in brown.categories()])

    
    data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)


    for inc in range(1,30):
        #print(inc-1, ":",count)
        count = 0
    #for word in sorted(data.conditions()):
        
        for word in sorted(data.conditions()):
            #print(count)
            #count = 0
            
            if len(data[word]) == inc:
            #if len(data[word].most_common()) == 3:
                tags = [tag for (tag, _) in data[word].most_common()]
    
            #if ((tags) == 3):]
            #if(len(tags) == 3):
            #print(tags)
                #for (_, 3) in data[word].most_common():
                #if data[word].most_common() == (tags,3):
                #print(word, ' '.join(tags))
                count = count + 1
            #temp = ' '.join(tags)

        print(inc, ":",count)


    #brown_sents = brown.sents(categories='news')
    #unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
    #unigram_tagger.tag(brown_sents[2007])

    #print(count)

main()
