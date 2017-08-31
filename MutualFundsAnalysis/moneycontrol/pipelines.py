# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings

class MongoDBPipeline(object):

    #function to establish connection with mongodb
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    #function to insert documents in the collection
    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            log.msg("Entry added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item
