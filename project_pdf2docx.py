from pdf2docx import Converter

pdfname=input("Enter the name of the pdf: ")
docxname=input("Enter the name for word file: ")

if(pdfname.endswith(".pdf")):
    cnv=Converter(pdfname)
else:
    cnv=Converter(pdfname+".pdf")
cnv.convert(docxname+".docx")
cnv.close()