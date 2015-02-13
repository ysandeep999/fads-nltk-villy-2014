import warnings
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from io import StringIO
warnings.filterwarnings("ignore")



def scrap_pdf(path):
    warnings.warn("deprecated", Warning)
    print("1")
    rsrcmgr = PDFResourceManager()
    print("2")
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    print("3")
    device = TextConverter(rsrcmgr, retstr)
    print("4")
    fp = open(path, 'rb')
    print("6")
    process_pdf(rsrcmgr, device, fp)
    print("5")
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    print("HI")
    return str

def fxn():
    ##a = "scrap_pdf('a3-rane.pdf')"
    warnings.warn("deprecated", Warning)
    
    

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    warnings.filterwarnings("ignore")
    #scrap_pdf("a3-rane.pdf")
    fxn()
    
    print(scrap_pdf("a3-rane.pdf"))

