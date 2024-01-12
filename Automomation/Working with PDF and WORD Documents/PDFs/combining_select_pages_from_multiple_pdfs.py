#! python3
import os
import PyPDF2

# Step 1: Find all PDF files
pdf_files = []

for filename in os.listdir('.'):  # return a list of every file in the current working directory.
    if filename.endswith('.pdf'):
        pdf_files.append(filename)

pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

for filename in pdf_files:
    pdffileobj = open(file=filename, mode='rb')
    pdf_reader = PyPDF2.PdfFileReader(pdffileobj)

    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

pdf_output = open('combined.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()