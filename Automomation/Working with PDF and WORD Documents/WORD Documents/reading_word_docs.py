#! Python 3

import docx

word_doc = "C:\\Users\\User\\Desktop\\Functional Safety\\Functional Safety\\My_Training Basics2\\Word Doc Version of PDF files\\ISO 26262 Functional Safety Requirement Types.docx"
doc = docx.Document(word_doc)
doc_paragraph_length = len(doc.paragraphs)
print(doc_paragraph_length)
for paragraph in range(doc_paragraph_length):
    print(doc.paragraphs[paragraph].text)
