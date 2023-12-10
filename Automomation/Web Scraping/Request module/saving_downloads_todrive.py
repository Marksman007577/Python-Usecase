# Shebang line for Windows OS
# ! python3

import requests as rq

# Open a web browser and download a file
URL = "https://www.gutenberg.org/cache/epub/1112/pg1112.txt"


def check_data_error(url_link):
    req_doc = rq.get(url_link)
    try:
        req_doc.raise_for_status()
    except Exception as exc:
        return exc


def request_data(url_link, page_start, page_end, func):
    req_doc = rq.get(url_link)
    req_doc_error = func
    doc_type = type(req_doc)
    doc_status = req_doc.status_code == rq.codes.ok
    doc_length = len(req_doc.text)
    doc_content = req_doc.text[page_start:page_end]
    return req_doc, doc_type, doc_status, doc_length, doc_content, req_doc_error


def write_data_2_file(data_content):
    with open('extractedFile.txt', mode='wb') as file:
        for chunk in data_content.iter_content(1000):
            file.write(chunk)
        file.close()


result = request_data(url_link=URL, page_start=0, page_end=350, func=check_data_error(url_link=URL))
print(result[3])
write_data_2_file(data_content=result[0])

