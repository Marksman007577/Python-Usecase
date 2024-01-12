import PyPDF2

# Extracting text from PDF
file = "C:\\Users\\User\\Desktop\\Easy Termination vodafone.de.pdf"
with open(file=file, mode='rb') as pdf_file:
    read_file = PyPDF2.PdfFileReader(pdf_file)
    num_pages = read_file.numPages
    first_page = read_file.getPage(0)
    print(first_page.extractText())
