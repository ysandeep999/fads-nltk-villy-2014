'''
import nltk
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
'''
from bs4 import BeautifulSoup
from urllib import request
#from bs4 import BeautifulSoup

def main():    
    url = "http://en.wikipedia.org/wiki/Albert_Einstein"
    html = request.urlopen(url).read().decode('utf8')
    raw = bs4.BeautifulSoup(html).get_text()
    stText = [txt for txt in raw]
    print(" ".join(stText))

    lst = []
    lst2 = []
    wrds = nltk.corpus.words.words('en')
    rexp = r'^[a-z]+$'
    for word in tokens:
        substr = re.findall(rexp,word)
        lst.append(substr)


    for w1 in lst:
        if w1 not in wrds:
            lst2.append(w1)
            
    #print(lst2)        
    #print(text[4567:5678])

                        
main()
