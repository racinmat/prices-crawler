import sqlite3


class Database:
    db = sqlite3.connect('prices_db')

    @staticmethod
    def insert_price(product, price, shop, time):
        cursor = Database.db.cursor()
        cursor.execute('''
        INSERT INTO prices(product, price, shop, time) VALUES (?, ?, ?, ?)
        ''', (product, price, shop, str(time)))
        Database.db.commit()
