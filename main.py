import threading

from alza_crawler import AlzaCrawler
from czc_crawler import CzcCrawler


def crawl():
    czcCrawler.crawl_site()
    alzaCrawler.crawl_site()
    threading.Timer(60 * 60 * 12, crawl).start()  # twice per day


if __name__ == '__main__':
    print('starting crawler')
    czcCrawler = CzcCrawler()
    alzaCrawler = AlzaCrawler()
    crawl()
