import re
import sqlite3

import yaml

import db
from crawler import Crawler


class CzcCrawler(Crawler):

    def __init__(self):
        self.name = 'czc'
        with open('config.yml') as f:
            self.products = yaml.load(f)['pages']['czc']

    def price_text_to_int(self, price):
        return int(''.join(re.findall('\d+', price)))

    def price_selector(self):
        return '#product-price-and-delivery-section > div.left > div.total-price > span.price.action > span.price-vatin'
