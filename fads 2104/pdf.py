from PyPDF2 import PdfFileReader,PdfFileWriter
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
def pdf2text(fname):
    pdf = PdfFileReader(open(fname,"rb"))
    con = ""
    for i in range(0, 10):
        con += pdf.getPage(i).extractText()
        con = " ".join(con.strip().split())
    #print(content)
    a,b = bigramandtrigram(con)
    return a,b
    
def bigramandtrigram(txt):
    text = nltk.word_tokenize(txt) 
    text1 = nltk.bigrams(text)
    text2 = nltk.trigrams(text)
    #fdist = nltk.FreqDist(text1)
    #fdist1 = nltk.FreqDist(text2)
    stopwords = set(nltk.corpus.stopwords.words("english"))
  
    bgram = [(x,y) for x,y in text1 if x.isalpha() and y.isalpha()
             and x.islower() and y.islower()
             and x not in stopwords and y not in stopwords]
    
    trigrm = [(a,b,c) for a,b,c in text2 if a.isalpha() and b.isalpha() and c.isalpha()
              and a.islower() and b.islower() and c.islower()
              and a not in stopwords and b not in stopwords and c not in stopwords]
    fdist = nltk.FreqDist(bgram)
    fdist1 = nltk.FreqDist(trigrm)
    print("Bigrams:")
    print(fdist.most_common(10))
    print()
    print("Trigrams:")
    print(fdist1.most_common(10))
    print()
    return fdist.most_common(10),fdist1.most_common(10)
    
def main():

    lst = []
    lst1 = []
    for i in range(1,6):
        path = input("Enter the input file:")
        path1 = path.encode("ascii","ignore")
        b,t = pdf2text(path1)
        lst.append(b)
        lst1.append(t)
    print("List of bigrams:")    
    print(lst)
    print()
    print("List of trigrams:")
    print(lst1)
        
    #text1 = "text1.pdf".encode("ascii","ignore")
    #text2 = "text2.pdf".encode("ascii","ignore")
    #text3 = "text3.pdf".encode("ascii","ignore")
    #text4 = "text4.pdf".encode("ascii","ignore")
    #text5 = "text5.pdf".encode("ascii","ignore")
    #print("PDF 1:")
    #b1,t1 = pdf2text(text1)
    #print("PDF 2:")
    #b2,t2 = pdf2text(text2)
    #print("PDF 3:")
    #b3,t3 = pdf2text(text3)
    #print("PDF 4:")
    #b4,t4 = pdf2text(text4)
    #print("PDF 5:")
    #b5,t5 = pdf2text(text5)
    
    input("Press enter to exit.")
main()    
