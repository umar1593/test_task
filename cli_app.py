from pprint import pprint

import requests
import validators


def add_protocol(str):
    if str[0:8] != 'https://' and str[0:7] != 'http://':
        return 'https://' + str
    return str


strings = [
    'jaafd',
    'aadfadsf',
    'google.com',
    'https://yandex.ru',
    'https://mvideo.ru',
    'https://aliexpress.com',
    'https://vk.com',
    'https://github.com',
]

urls = [add_protocol(str) for str in strings if validators.url(str)]


url_methods = {}

for url_original in urls:
    methods = {}
    response = requests.get(url_original)
    if response.status_code != 405:
        methods['GET'] = response.status_code

    response = requests.post(url_original)
    if response.status_code != 405:
        methods['POST'] = response.status_code

    response = requests.put(url_original)
    if response.status_code != 405:
        methods['PUT'] = response.status_code

    response = requests.patch(url_original)
    if response.status_code != 405:
        methods['PATCH'] = response.status_code

    response = requests.head(url_original)
    if response.status_code != 405:
        methods['HEAD'] = response.status_code

    response = requests.options(url_original)
    if response.status_code != 405:
        methods['OPTIONS'] = response.status_code

    response = requests.delete(url_original)
    if response.status_code != 405:
        methods['DELETE'] = response.status_code

    url_methods[url_original] = methods

pprint(url_methods)
