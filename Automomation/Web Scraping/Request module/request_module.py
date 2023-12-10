# Shebang line for Windows OS
# ! python3

import requests as rq

# Open a web browser and download a file
URL = "https://www.gutenberg.org/cache/epub/1112/pg1112.txt"


def request_data(url_link, page_start, page_end):
    req_doc = rq.get(url_link)
    doc_type = type(req_doc)
    doc_status = req_doc.status_code == rq.codes.ok
    doc_length = len(req_doc.text)
    doc_content = req_doc.text[page_start:page_end]
    return doc_type, doc_status, doc_length, doc_content


result = request_data(URL, 0, 250)
print('The Document type is:', result[0])
print('The Document download success status is:', result[1])
print('The Document length is:', result[2])
print('The Document content is:\n', result[3])
