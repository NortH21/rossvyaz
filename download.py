#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import requests

logging.basicConfig(level=logging.INFO)

CSV = ['Kody_ABC-4kh.csv', 'Kody_DEF-9kh.csv']
URL = 'https://www.rossvyaz.ru/opendata/7710549038-Rosnumbase/'
HEADERS = {'user-agent': 'dwn-csv/0.0.1'}
CATALOG = './csv/'

def get_csv():
    try:
        for i in range(len(CSV)):
            logging.debug(f'Print url = {URL + CSV[i]}')
            data = requests.get(URL + CSV[i], HEADERS)
            write_file(id=CSV[i], csv=data)
    except:
        logging.error(f'Cannot download csv')

def write_file(id, csv):
    try:
        with open(CATALOG + id, "wb") as f:
            f.write(csv.content)
    except:
        logging.error(f'Cannot write csv')

def main():
    get_csv()

if __name__ == "__main__":
    main()
