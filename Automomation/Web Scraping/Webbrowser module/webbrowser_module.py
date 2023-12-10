# Shebang line for Windows OS
# ! python3

import webbrowser as wb

# Open a web browser
URL = wb.open("https://google.com/")

# Open multiple browsers homepage
FACEBOOK = "https://facebook.com/"
TWITTER = "https://twitter.com/"
YAHOOMAIL = "https://yahoomail.com/"
GMAIL = "https://gmail.com/"

URL_list = [FACEBOOK, TWITTER, YAHOOMAIL, GMAIL]

for url in URL_list:
    wb.open(url)

