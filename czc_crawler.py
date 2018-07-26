import re
import requests
import sqlite3

import yaml
from lxml import html

import db
from crawler import Crawler


class CzcCrawler(Crawler):

    def __init__(self):
        self.name = 'czc'
        with open('config.yml') as f:
            self.products = yaml.load(f)['pages']['czc']

    def get_price(self, page):
        content = html.fromstring(requests.get(page).content)
        return self.price_text_to_int(content.cssselect(self.price_selector())[-1].text)

    def price_text_to_int(self, price):
        return int(''.join(re.findall('\d+', price)))

    def price_selector(self):
        return '#product-price-and-delivery-section > div.left > div.total-price > span > span.price-vatin'
