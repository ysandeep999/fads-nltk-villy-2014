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


def show_freq_occur_words_with_val(common):
    
    for tuples in common:
        print(tuples[0])


def calc_freq(data):
    
    fdist_b = nltk.FreqDist(data)
    return fdist_b


def common10(fdist):
    
    common = fdist.most_common(10)
    return common


def del_stop_bi(words):
    
    stopwords = set(nltk.corpus.stopwords.words("english"))
    
    tup_non_stop = [(x,y) for x,y in words
                    if x.isalpha() and y.isalpha()
                         and x.islower() and y.islower()
                         and len(x) > 2 and len(y) > 2
                         and x not in stopwords and y not in stopwords]
    
    return tup_non_stop


def del_stop_tri(words):
    
    stopwords = set(nltk.corpus.stopwords.words("english"))    
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

    #remove stopwords for bigram and trigram
    bi_not_stop = del_stop_bi(bi_store)
    tri_not_stop = del_stop_tri(tri_store)

    # Calculate frequency distribution
    bi_common = calc_freq(bi_not_stop)
    tri_common = calc_freq(tri_not_stop)
    
    # Finding 10 most common words in bigrams and trigrams
    bi_common_tups = common10(bi_common)
    tri_common_tups = common10(tri_common)

    # Show output
    show_freq_occur_words_with_val(bi_common_tups)
    print("-----------------")
    show_freq_occur_words_with_val(tri_common_tups)
    

def pdf_to_text(path):
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
    string = retstr.getvalue()
    retstr.close()
    return string


   

def main():
    
    all_txt = ""
    pdf_file_names = ["a3-rane.pdf","a4-jimenez.pdf", "a6-wu.pdf",
                      "a7-ravishankar.pdf", "a8-shun.pdf"]

    for pdf_file in pdf_file_names:
        text_from_pdf = pdf_to_text(pdf_file)
        mining_data(text_from_pdf)
        all_txt = all_txt + text_from_pdf


main()



