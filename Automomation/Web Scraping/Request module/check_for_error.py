# Shebang line for Windows OS
# ! python3

import requests as rq

# Open a web browser and download a file
URL = "https://inventwithpython.com/page_that_does_not_exist"


def check_data_error(url_link):
    req_doc = rq.get(url_link)
    try:
        req_doc.raise_for_status()
    except Exception as exc:
        return exc


result = check_data_error(URL)
print(result)
