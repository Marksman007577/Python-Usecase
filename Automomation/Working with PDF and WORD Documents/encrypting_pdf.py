import PyPDF2

# Extracting text from PDF
file = "C:\\Users\\User\\Desktop\\AI\\The Best ChatGPT Cheat Sheets.pdf"
with open(file=file, mode='rb') as pdf_file:
    read_file = PyPDF2.PdfFileReader(open(file=file, mode='rb'))

# Create an empty PDF document instance
new_PDF = PyPDF2.PdfFileWriter()

for page_num in range(read_file.numPages):
    new_PDF.addPage(read_file.getPage(page_num))

new_PDF.encrypt('swordfish')
with open(file='encrypted_doc.pdf', mode='wb') as encrypted_file:
    new_PDF.write(encrypted_file)
    encrypted_file.close()

pdf_file.close()