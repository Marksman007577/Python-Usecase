import PyPDF2

# Decrypting PDF File
file = "C:\\Users\\User\\Desktop\\Easy Termination vodafone.de.pdf"
with open(file=file, mode='rb') as pdf_file:
    read_file = PyPDF2.PdfFileReader(open(file=file, mode='rb'))
    read_file.decrypt(password='rosebud')
    num_pages = read_file.numPages
    first_page = read_file.getPage(0)
    print(first_page.extractText())
