# -*- coding: utf-8 -*-
import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

SOURCES = [
    '2013.csv',
    '2015.csv',
    '2016.csv',
    '2017.csv',
    '2018.csv',
    '2019.csv'
]

URLS_FILE = 'news_sources.txt'

KEY_WORDS_ACTION = [
    'убита',
    'убил',
    'зарезал',
    'прикончил',
    'скончалась',
    'убийств',
    'расправ',
    'смерт',
]

KEY_WORDS_SUBJECT = [
    'девушк',
    'женщин',
    'девушек',
    'девочк',
    'девочек',
    'баб',
    'старушк',
    'любовниц',
    'женa',
    'жену',
    'жены'
    'сожительниц'
]

BLACK_LIST = [
    'ru.wikipedia.org',
    'wikipedia.org',
]

SKIP_UNTIL = ''
