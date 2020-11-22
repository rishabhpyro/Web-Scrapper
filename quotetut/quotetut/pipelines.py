# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# import sqlite3
# import mysql.connector
import pymongo


class QuotetutPipeline:
    def __init__(self):

        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )

        db = self.conn['myquotes']
        self.collection = db['quotes_db']

        # Code not be used in case of Mongo DB
        # self.create_connection()
        # self.create_table()

    # def create_connection(self):
    #     # Code while usingg sqlite3
    #     # self.conn = sqlite3.connect()
    #
    #     # Code while using mysql
    #     # self.conn = mysql.connector.connect(
    #     #     host='localhost',
    #     #     user='root',
    #     #     passwd='rishabhtestpython',
    #     #     database='myquotes'
    #     # )
    #     # self.curr = self.conn.cursor()

    # def create_table(self):
    #     self.curr.execute("""drop table if exists quotes_db""")
    #     self.curr.execute("""create table quotes_db(
    #                 title text,
    #                 author text,
    #                 tag text
    #                 )""")

    def process_item(self, item, spider):
        self.collection.insert(dict(item))

        # Code used in mysql or sqlite
        # self.store_db(item)

        return item

    # def store_db(self, item):
    #
    #     # Code while using sqlite3
    #     # self.curr.execute("""insert into quotes_db values(?,?,?)""", (
    #     #     item['title'][0],
    #     #     item['author'][0],
    #     #     item['tag'][0]
    #     # ))
    #
    #     # Code while usign mysql
    #     # self.curr.execute("""insert into quotes_db values(%s,%s,%s)""", (
    #     #     item['title'][0],
    #     #     item['author'][0],
    #     #     item['tag'][0]
    #     # ))
    #     self.conn.commit()
