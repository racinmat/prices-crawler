import threading

from alza_crawler import AlzaCrawler
from czc_crawler import CzcCrawler


def do_stuff():
    print('done stuff, waiting')


def do_stuff_repeated():
    do_stuff()
    threading.Timer(5, do_stuff_repeated).start()  # twice per day


if __name__ == '__main__':
    print('starting doing stuff')
    do_stuff_repeated()
