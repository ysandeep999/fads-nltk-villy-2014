import nltk
from nltk.corpus import stopwords 
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from io import StringIO
from nltk.util import ngrams



# function displays bigrams and trigrams from all pdf's
def show_output_for_all_pdf(all_txt):
    l =[]
    a,b = mining_data(all_txt) 
    l.append(("all pdf's",a,b))
    return show_output(l)


# function prints output
def show_output(data_in_list):
    for items in data_in_list:
        print("----------",items[0],"-----------\n\n")
        print("bigrams are:\n")
        for tup_bi in items[1]:
            print(tup_bi)
        print("\n")
        print("trigrams are:\n")
        for tup_tri in items[2]:
            print(tup_tri)
        print("\n\n\n")


# function extracts required data after mining
def get_freq_occur_words_without_val(common):

    temp_lst = []
    for tuples in common:
        temp_lst.append(tuples[0])

    return temp_lst


# function calculates frequency distribution of input data
def calc_freq(data):
    
    fdist_b = nltk.FreqDist(data)
    return fdist_b


# Function finds n most common words
def common(fdist,n):
    
    common = fdist.most_common(n)
    return common


# Funiction initialize stopwords
def init_stop():
    
    global stopwords
    stopwords = set(nltk.corpus.stopwords.words("english"))
    
    
# function remove stopwords for bigram input
def del_stop_bi(words):
    
    global stopwords    
    tup_non_stop = [(x,y) for x,y in words
                    if x.isalpha() and y.isalpha()
                         and x.islower() and y.islower()
                         and len(x) > 2 and len(y) > 2
                         and x not in stopwords and y not in stopwords]
    
    return tup_non_stop


# function remove stopwords for trigram input
def del_stop_tri(words):
    
    global stopwords
    tup_non_stop = [(x,y,z) for x,y,z in words
                    if x.isalpha() and y.isalpha()
                        and z.isalpha()
                        and x.islower() and y.islower() and z.islower()
                        and len(x) > 2 and len(y) > 2 and len(z) > 2
                        and x not in stopwords and y not in stopwords
                        and z not in stopwords]

    return tup_non_stop
    
    

def mining_data(text): 

    # Tokenize every word in text
    wrd = nltk.word_tokenize(text)

    #Do bigrams and trigrams
    bi_store = nltk.bigrams(wrd)
    tri_store = nltk.trigrams(wrd)

    # initialize stopwords
    init_stop()

    #remove stopwords for bigram and trigram
    bi_not_stop = del_stop_bi(bi_store)
    tri_not_stop = del_stop_tri(tri_store)

    # Calculate frequency distribution
    bi_freq = calc_freq(bi_not_stop)
    tri_freq = calc_freq(tri_not_stop)
    
    # Finding 10 most common words in bigrams and trigrams
    bi_common_tups = common(bi_freq,10)
    tri_common_tups = common(tri_freq,10)

    # extract required final data
    bi_in_data = get_freq_occur_words_without_val(bi_common_tups)
    tri_in_data = get_freq_occur_words_without_val(tri_common_tups)

    return bi_in_data, tri_in_data

    

# function extracts text from pdf
def pdf_to_text(path):
    
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()
    string = retstr.getvalue()
    retstr.close()
    return string


   

def main():

    lst = []
    all_txt = ""
    pdf_file_names = ["a6-wu.pdf","a7-ravishankar.pdf", "a8-shun.pdf",
                      "a3-rane.pdf","a4-jimenez.pdf"]

    pdf_name = ["daa.pdf"]

    for pdf_file in pdf_name:
        text_from_pdf = pdf_to_text(pdf_name)
        all_txt = all_txt + "\n" + text_from_pdf
        a_2,b_3 = mining_data(text_from_pdf)
        lst.append((pdf_file,a_2,b_3))
        


    show_output(lst)

    #show_output_for_all_pdf(all_txt)


main()



