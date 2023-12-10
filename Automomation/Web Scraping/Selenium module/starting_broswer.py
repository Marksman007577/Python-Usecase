from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
exec_path = r"C:\Program Files (x86)\geckodriver.exe"


def open_browser(browser_type):
    if browser_type.title() == ' ':
        return
    elif browser_type.title() == 'Firefox':
        url = webdriver.Firefox(executable_path=exec_path, options=options)
        return url.get('https://inventwithpython.com/')


def find_element_on_page(browser_type):
    if browser_type.title() == ' ':
        return
    elif browser_type.title() == 'Firefox':
        url = webdriver.Firefox(executable_path=exec_path, options=options)
        web = url.get('https://inventwithpython.com/')
        try:
            elem = url.find_element_by_class_name('bookcover')
            print('Found <%s> element with that class name!', elem.tag_name)
        except:
            print('Was not able to find an element with that name.')


def click_a_page(browser_type):
    if browser_type.title() == ' ':
        return
    elif browser_type.title() == 'Firefox':
        url = webdriver.Firefox(executable_path=exec_path, options=options)
        web = url.get('https://inventwithpython.com/')
        link_elem = url.find_element_by_link_text('Read for Free')
        return link_elem.click()


def filling_submit_forms(browser_type):
    if browser_type.title() == ' ':
        return
    elif browser_type.title() == 'Firefox':
        url = webdriver.Firefox(executable_path=exec_path, options=options)
        web = url.get('https://gmail.com/')
        emailelem = web.find_element_by_id('Email or phone')
        emailelem.send_keys('xxx@gmail.com')
        passwordelem = web.find_element_by_id('Passwd')
        passwordelem.send_keys('12345')
        passwordelem.submit()


# open_browser(browser_type='firefox')
# find_element_on_page(browser_type='firefox')
# click_a_page(browser_type='firefox')
# filling_submit_forms(browser_type='firefox')
