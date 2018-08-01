import abc
import datetime
import requests
from lxml import html

import db
from lxml.cssselect import CSSSelector


class Crawler:
    products = {}
    name = ''

    def crawl_site(self):
        for product, page in self.products.items():
            try:
                price = self.get_price(page)
                db.Database.insert_price(product, price, self.name, datetime.datetime.now())
            except:
                db.Database.insert_price(product, None, self.name, datetime.datetime.now())
                print('Product {} on page {} does not exist, skipping'.format(product, page))

    @abc.abstractmethod
    def get_price(self, page):
        pass

    @abc.abstractmethod
    def price_text_to_int(self, price):
        pass

    @abc.abstractmethod
    def price_selector(self):
        pass
