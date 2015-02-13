import nltk
from nltk.book import *
from nltk.corpus import stopwords

'''
def stop(text):
    fdist = FreqDist(text)
    stopwords = set(nltk.corpus.stopwords.words("english"))

    content = [w for w in fdist if w.isalpha() and w.islower() not in stopwords]
    
    print(content[:50])

#stop(text7) 
################################################################################
'''


txt = """While carrying a debit or credit card makes our life simpler, many a times it can be a bummer. Especially when you are in a store in front of people and trying to make a payment and the swipe gets declined.

    With our increasing dependency on credit and debit cards, we have grown used to not carrying cash around. We have also realised the importance of credit cards over cash. But, when you are out there throwing a dinner party to your friends and try to make a credit card payment and if the transaction gets declined, it can be an embarrassment.

    There are many reasons why a credit card swipe can be declined. We have listed the top eight reasons for such a refusal of payment"""

def bigram(text):
    
    store = nltk.bigrams(text)
    fdist_b = FreqDist(store)
    stopwords = set(nltk.corpus.stopwords.words("english"))

    bgram = [(x,y) for x,y in fdist_b if x.isalpha() and y.isalpha()
             and x.islower() and y.islower()
             and x not in stopwords and y not in stopwords]

    print(bgram[:50])
    input("press enter to exit")
    '''
    for bigr in fdist_b:
        for stopw in stopwords:
            if (bigr == stopw):
               print ("Bad bigram = ", bigr)
            else:
               no_stop = bigr
               print ("Bigrams with out stopwords = ",no_stop)

#    print ("Bigrams with out stopwords = ",no_stop)        
    
#    print(fdist_b.most_common(50))
'''
bigram(txt)



