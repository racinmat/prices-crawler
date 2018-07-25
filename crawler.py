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
            price = self.get_price(page)
            db.Database.insert_price(product, price, self.name, datetime.datetime.now())

    def get_price(self, page):
        content = html.fromstring(requests.get(page).content)
        return self.price_text_to_int(content.cssselect(self.price_selector())[0].text)

    @abc.abstractmethod
    def price_text_to_int(self, price):
        pass

    @abc.abstractmethod
    def price_selector(self):
        pass
