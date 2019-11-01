# -*- coding: utf-8 -*-
import config

import logging
import re

import joblib as joblib
import pandas as pd
from urllib.parse import urlparse


if __name__ == '__main__':
    logging.basicConfig(filename='extract_sites.log', level='DEBUG')

    result = []
    for f_name in config.SOURCES:
        df = pd.read_csv(f_name)
        raw_urls = df['ссылки и дополнения'].tolist()

        for url_str in raw_urls:
            if url_str and (type(url_str) is str and url_str.strip() != ''):
                url = re.findall(r'(https?://\S+)', url_str)
                if len(url) == 0:
                    continue
                url = url[0].replace('www.', '')
                domain = urlparse(url).netloc
                # print(domain)
                result.append(domain)

                main_domain = '.'.join(domain.split('.')[-2:])
                if main_domain != domain:
                    result.append(main_domain)

    res_set = sorted(set(result))

    with open(config.URLS_FILE, 'w') as f:
        for r in res_set:
            print(r)
            logging.info(r)
            print(r, file=f)

    joblib.dump(res_set, config.URLS_FILE+'.pkl')



