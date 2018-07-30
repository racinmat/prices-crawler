import sqlite3


class Database:

    @staticmethod
    def insert_price(product, price, shop, time):
        db = sqlite3.connect('prices_db')
        cursor = db.cursor()
        cursor.execute('''
        INSERT INTO prices(product, price, shop, time) VALUES (?, ?, ?, ?)
        ''', (product, price, shop, str(time)))
        db.commit()
        db.close()
