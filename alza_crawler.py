import re

import yaml

from crawler import Crawler


class AlzaCrawler(Crawler):

    def __init__(self):
        self.name = 'alza'
        with open('config.yml') as f:
            self.products = yaml.load(f)['pages']['alza']

    def price_text_to_int(self, price):
        int(''.join(re.findall('\d+', price)))

    def price_selector(self):
        return '#prices > tr.pricebaseguarantee.noimage > td > div > div > div:nth-child(1) > div.colValue > span'
