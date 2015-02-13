# This program does stripping off the html and saves the text without the markup
from bs4 import BeautifulSoup
import nltk, re, pprint, nltk.corpus
from nltk import word_tokenize
from urllib import request
import os

def main():    
    url = "http://en.wikipedia.org/wiki/Albert_Einstein"
    html = request.urlopen(url).read().decode('utf8')
    raw = BeautifulSoup(html).get_text()
    text = [txt for txt in raw]
    text = "".join(text)
    print(text)
main()
