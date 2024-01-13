#! python 3

import docx

word_doc = "C:\\Users\\User\\Desktop\\Functional Safety\\FTA\\FTA Basics.docx"


def get_text(file_name):
    doc_file = docx.Document(file_name)
    full_text = []
    for paragraph in doc_file.paragraphs:
        full_text.append(' ' + paragraph.text)
    return '\n'.join(full_text)


doc_content = get_text(file_name=word_doc)
print(doc_content)
