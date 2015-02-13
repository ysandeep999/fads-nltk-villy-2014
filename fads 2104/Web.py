#NLTK Chapter-3
#Assignment 13
#Simhachalam Panduri paired with Sri Harsha Kilari
#Use Python and Beautiful Soup to strip off the html and save the text without the markup.
import nltk
from urllib import request
from nltk import word_tokenize
from nltk.corpus import words
from bs4 import BeautifulSoup
import re
url = "http://www.nltk.org/book/ch01.html"
def unknown(url):
    html = request.urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html).get_text()
    tokens = set(word_tokenize(raw))
    tokens = list(tokens)
    lst = []
    lst2 = []
    wrds = nltk.corpus.words.words('en')
    rexp = r'^[a-z]+$'
    for word in tokens:
        substr = re.findall(rexp,word)
        if len(substr) > 0:
            lst.append(substr[0])

    for w1 in lst:
        if w1 in wrds:
            a = 0
        else:
            lst2.append(w1)
    print(lst2)
    print(len(lst2))

unknown(url)

#a = len(tokens)
#print(tokens)
#print("We have ",a, "words in the HTML page")
#tokens = tokens[50:5000]
#text = nltk.Text(tokens)
#print(text)'''

