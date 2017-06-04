'''from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys,getopt


def convert(fname, pages=None):
    if not pages:
        pagenums=set()
    else:
        pagenums=set(pages)


    output=StringIO()
    manager=PDFResourceManager()
    converter=TextConverter(manager, output, laparams=LAParams())
    interpreter=PDFPageInterpreter(manager, converter)

    infile=file(fname,'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text=output.getvalue()
    output.close
    return text

def convertMultiple(pdfDir,txtDir):
    if pdfDir=="":pdfDir=os.getcwd() +"\\"
    for pdf in os.listdir(pdfDir):
        fileExtension=pdf.split(".")[-1]
        if fileExtension=="pdf":
            pdfFilename=pdfDir+pdf
            text=convert(pdfFilename)
            textFilename=txtDir+pdf+".txt"
            textFile=open(textFilename,"w")
            textFile.write(text)

pdfDir="C:/pdftotxt/pdfs/"
txtDir="C:/pdftotxt/txt/"
convertMultiple(pdfDir, txtDir)'''

"""import pyPdf

def getPDFContent(path):
    content=""

    pdf=pyPdf.PdfFileReader(file(path,"rb"))
    for i in range(0,pdf.getNumPages()):
        content+=pdf.getPage(i).extractText() + "\n"

    content="".join(content.replace(u"\xa0"," ").strip().split())
    return content

print getPDFContent("Documents1.pdf").encode("ascii","ignore")
    
"""
import pyPdf
pdf_file=open('Internship offer letter.pdf')
read_pdf=pyPdf.PdfFileReader(pdf_file)

number_of_pages=read_pdf.getNumPages()
print number_of_pages


pdf_file=open('Internship offer letter.pdf')
read_pdf = pyPdf.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
print page_content
