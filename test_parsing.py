import validators

from cli_app import add_protocol

strings_list = [
    'jaafd',
    'aadfadsf',
    'google.com',
    'https://yandex.ru',
    'https://mvideo.ru',
    'https://aliexpress.com',
    'https://vk.com',
    'https://github.com',
]

str = 'google.com'

valid_list = [
    'https://yandex.ru',
    'https://mvideo.ru',
    'https://aliexpress.com',
    'https://vk.com',
    'https://github.com',
]


def test_add_protocol():
    assert add_protocol(str) == 'https://google.com'


def test_valid_links():
    valid_links = [i for i in strings_list if validators.url(i)]
    assert valid_links == valid_list
