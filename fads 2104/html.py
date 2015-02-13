from bs4 import BeautifulSoup
import nltk, re, pprint, nltk.corpus
from nltk import word_tokenize
from urllib import request


def main():    
    url = "http://www.nltk.org/book/ch01.html"
    html = request.urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html).get_text()
    text = [txt for txt in raw]
    print("".join(text))
          
main()
