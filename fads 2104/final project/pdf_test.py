# testing with pdf
import os

import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader


def main():
    output = PdfFileWriter()
    input1 = PdfFileReader(open("134.pdf", "rb"))
    no_of_pages = input1.getNumPages()

    p =  PyPDF2.pdf.PageObject(input1)
    ##print(p.getContents())
    #print(p.extractText())
    ##print(no_of_pages)
    print(input1.getPage(0).extractText())

    # add page 1 from input1 to output document, unchanged
    output.addPage(input1.getPage(3))
    ##print(output)


    # finally, write "output" to document-output.pdf
    outputStream = ("PyPDF2-output.pdf", "wb")
    #output.write(outputStream)


main()
