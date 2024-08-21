import PyPDF2
import os
import time

print("\nGreetings Sir/Mam, Your good name please....")
name=input("\nPlease Enter your name: ")
print(f"\nHello {name}, Welcome to the PDF Merger created by Mr. Vishwas Gandham.\nPlease provide the required details. [Note: To STOP the program, type \"DONE\" when asked for Merged PDF's name.]")


while(True):
    pdfs=[(pdfs) for pdfs in input("\n\nEnter the PDF names separated by single white space (CAUTION: Trying to enter the name in new line can end the program or may give error): ").split()]
    if(pdfs.lower()=="done"):
        break
    
    new_pdf=input("\nEnter the desired name for your Merged PDF: ")
    if(new_pdf.lower()=="done"):
        break

    merger=PyPDF2.PdfMerger()
    for filename in pdfs:
        pdfFile= open(filename, 'rb')
        pdfReader=PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
    pdfFile.close()
    merger.write(new_pdf)
    print("\nPDF has been merged successfully.\nThank You!")
    
    print("\n-x- END OF THE PROGRAM -x-")
    time.sleep(2)
    os.startfile(new_pdf)

