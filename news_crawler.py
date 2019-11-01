# -*- coding: utf-8 -*-
import logging
import traceback

import joblib
import newspaper

import tqdm

import config
from check_dup import check_existance


if __name__ == '__main__':
    logging.basicConfig(filename='news_crawler.log', level='INFO')

    sources = joblib.load('sources.pkl')

    with open('news_sources.txt', 'r') as f:
        sources = f.read().split('\n')

    for source_url in sources:
        if source_url < config.SKIP_UNTIL:
            print(F'Skipping: {source_url}')
            logging.info(F'Skipping {source_url}')
            continue
        if any([source_url in bl for bl in config.BLACK_LIST]):
            print(F'Skipping: {source_url}. (Blacklisted)')
            logging.info(F'Skipping {source_url}. (Blacklisted)')
            continue

        paper = newspaper.build('http://www.' + source_url, language='ru')
        print('-'*30 + source_url + '-'*30)
        print('-'*30 + 'size: '+ str(paper.size()) + '-'*30)
        logging.info('-'*30 + source_url + '-'*30)
        logging.info('-'*30 + 'size: '+ str(paper.size()) + '-'*30)

        for article in tqdm.tqdm(paper.articles):
            try:
                article.download()
                article.parse()

                text = F"{article.title}\n{article.meta_description}\n{article.text}"

                if any([w in text for w in config.KEY_WORDS_ACTION]) \
                        and any([w in text for w in config.KEY_WORDS_SUBJECT]) \
                        and not check_existance(article.url):
                    logging.info(article.url)
                    print(F"\n{article.url}\n")
            except Exception as e:
                traceback.print_exc()
                logging.error(e, exc_info=True)

        print('='*30 + source_url + '='*30)
        logging.info('='*30 + source_url + '='*30)