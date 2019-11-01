# -*- coding: utf-8 -*-
import config
import pandas as pd


def check_existance(target: str) -> bool:
    print(F'Searching for {target}')

    for f_name in config.SOURCES:
        df = pd.read_csv(f_name)
        raw_urls = df['ссылки и дополнения'].tolist()

        for url_str in raw_urls:
            if type(url_str) is float:
                continue
            if target in url_str:
                print(F'It is already in the file {f_name}: ')
                print(df[df['ссылки и дополнения' == url_str]])
                return True
    return False


if __name__ == '__main__':
    target = input('Print the link:\n').strip().replace('https://', '').replace('www', '').replace('http://', '')
