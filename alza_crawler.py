import re
import requests

import yaml
from lxml import html

from crawler import Crawler


class AlzaCrawler(Crawler):

    def __init__(self):
        self.name = 'alza'
        with open('config.yml') as f:
            self.products = yaml.load(f)['pages']['alza']

    def get_price(self, page):
        content = html.fromstring(requests.get(page).content)
        return self.price_text_to_int(content.cssselect(self.price_selector())[0].text)

    def price_text_to_int(self, price):
        return int(''.join(re.findall('\d+', price)))

    def price_selector(self):
        return '#prices span.price_withVat'
