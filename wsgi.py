import re
from multiprocessing import Process
from time import sleep

from flask import Flask

from news_crawler import crawl

application = Flask(__name__)

_link = re.compile(r'(https?://\S+)', re.I)


def convert_links(text):
    def replace(match):
        groups = match.groups()
        return '<a href="{0}" target="_blank">{0}</a>'.format(groups[0])
    return _link.sub(replace, text)


@application.route("/")
def hello():
    with open('interesting_links.txt', 'r') as f:
        return '<br/>\r\n'.join(convert_links(f.read()).split('\n'))


if __name__ == "__main__":
    p = Process(target=crawl, args=())
    p.start()
    sleep(5)
    application.run()
