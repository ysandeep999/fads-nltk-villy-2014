# Final project
import PyPDF2 as pdf
inputfile = open("tst1.pdf","rb")
reader = pdf.PdfFileReader(inputfile)
print(reader)
pagex = reader.getPage(40)
print(type(pagex))
pagex.extractText()
