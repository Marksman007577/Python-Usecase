import bs4
import requests as rq


def data_extraction(url_link):
    link_res = rq.get(url_link)
    link_status = link_res.status_code == rq.codes.ok
    html_res = bs4.BeautifulSoup(link_res.text)
    html_type = type(html_res)
    return link_res, link_status, html_res, html_type


def find_html_element(html_doc, element):
    with open(html_doc, mode='r') as file:
        doc_soup = bs4.BeautifulSoup(file.read())
        elems = doc_soup.select('#' + element)
        elems_type = type(elems)
        elems_len = len(elems)
        elem_text = elems[0].getText()
        elems_string = str(elems[0])
        elems_attr = elems[0].attrs
    return elems, elems_type, elems_len, elem_text, elems_string, elems_attr


def data_from_element_attr(html_doc, element, index_num):
    with open(html_doc, mode='r') as file:
        doc_soup = bs4.BeautifulSoup(file.read())
        attr_elems = doc_soup.select(element)[index_num]
        attr_elems_string = str(attr_elems)
        attr_elems_attr = attr_elems.attrs
        key_list = []
        value_list = []
        for key, value in attr_elems_attr.items():
            key_list.append(key)
            value_list.append(value)

    return attr_elems, attr_elems_string, key_list, value_list


URL = 'https://github.com/Marksman007577'
result = data_extraction(url_link=URL)

print('The link obtained is:', result[0])
print('The status obtained is:', result[1])
print('The content obtained is:', result[2])
print('The content obtained is:', result[3])
print('\n')
print('Information found from the extracted element are listed below as:')
ans = find_html_element(html_doc='example.html', element='author')
for i in range(len(ans)):
    print(ans[i])

print('\n')
print('Information found from the extracted element are listed below as:')
answer = data_from_element_attr(html_doc='example.html', element='span', index_num=0)
for i in range(len(answer)):
    print(answer[i])
