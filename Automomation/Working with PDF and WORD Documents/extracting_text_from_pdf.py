import PyPDF2

PDF_file = open("C:\\Users\\User\\Desktop\\Easy Termination vodafone.de.pdf", mode='rb')
pdfReader = PyPDF2.PdfFileReader(PDF_file)
pages = pdfReader.numPages
print(pages)
page_obj = pdfReader.getPage(0)
print(page_obj)
print(page_obj.extractText())
