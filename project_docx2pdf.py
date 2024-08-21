from docx2pdf import convert

docxname=input("Enter the name of the word file: ")
pdfname=input("Enter the name for pdf: ")

try:
    if(docxname.endswith(".docx")):
        convert(docxname, pdfname+".pdf")
    else:
        convert(docxname+".docx", pdfname+".pdf")
except Exception as e:
    print(f"Error: {e}") 