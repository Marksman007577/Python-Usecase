import PyPDF2

# Extracting text from PDF
file = "C:\\Users\\User\\Desktop\\Functional Safety\\ASPICE\\AutomotiveSPICE_PAM_31.pdf"
with open(file=file, mode='rb') as pdf_file:
    read_file = PyPDF2.PdfFileReader(open(file=file, mode='rb'))

# Get the page(s) you want to rotate
page = read_file.getPage(0)

# Rotate the page
rotated_page = page.rotateClockwise(90)

# Create an empty PDF document instance
new_PDF = PyPDF2.PdfFileWriter()

# Add the rotated page to the empty document
new_PDF.addPage(rotated_page)

# Save the new PDF document
with open(file='rotated_page_doc.pdf', mode='wb') as new_file:
    new_PDF.write(new_file)

new_file.close()
pdf_file.close()
