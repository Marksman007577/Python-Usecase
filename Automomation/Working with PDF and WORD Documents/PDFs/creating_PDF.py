import PyPDF2

# Extracting text from PDF
file = "C:\\Users\\User\\Desktop\\Functional Safety\\ASPICE\\AutomotiveSPICE_PAM_31.pdf"
with open(file=file, mode='rb') as pdf_file:
    read_file = PyPDF2.PdfFileReader(open(file=file, mode='rb'))

# Create an empty PDF
empty_PDF = PyPDF2.PdfFileWriter()

# Copy pages from source
for page in range(read_file.numPages):
    num_pages = read_file.getPage(page)
    empty_PDF.addPage(num_pages)

# Copy to new PDF file
with open(file='New_Doc.pdf', mode='wb') as new_pdf_file:
    empty_PDF.write(new_pdf_file)
    new_pdf_file.close()

