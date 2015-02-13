import nltk
#from nltk.book import *
from nltk.corpus import stopwords
 
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from io import StringIO


txt = "hello how are you dear. and what is your bucket hello how are you"

def bigram(text):

    
    stopwords = set(nltk.corpus.stopwords.words("english"))
    wrd = [words for words in text.split(" ")]

    not_stop = [w for w in wrd if w not in stopwords
                and w.isalpha() and w.islower() and len(w)>2]
    
    ###print(wrd)
    store = nltk.bigrams(not_stop)
    ###print(store)
    fdist_b = nltk.FreqDist(store)

    common = fdist_b.most_common(20)


    for tuples in common:
        print(tuples[0])
    ###print(fdist_b)
    

    


    bgram = [(x,y) for x,y in fdist_b if x.isalpha() and y.isalpha()
             and x.islower() and y.islower()
             and x not in stopwords and y not in stopwords]
     

    ###print(bgram)
    #input("press enter to exit")



def scrap_pdf(path):
    """From http://stackoverflow.com/a/8325135/39040."""
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str


   

def main():
    
    #bigram(txt)
    ##f = open("temp.txt","r+b")
    ##for line in f:
      ##  print(line)
    all_txt = ""
    pdf_file_names = ["a3-rane.pdf","a4-jimenez.pdf", "a6-wu.pdf",
                      "a7-ravishankar.pdf", "a8-shun.pdf"]

    for pdf_file in pdf_file_names:
        all_txt = all_txt + scrap_pdf(pdf_file)
    bigram(all_txt)


main()



