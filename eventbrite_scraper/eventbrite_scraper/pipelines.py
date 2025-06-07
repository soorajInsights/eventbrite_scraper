# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class EventbritePipeline:
    def open_spider(self, spider):
        self.file = open('events.json', 'w', encoding='utf-8')
        self.file.write("[\n")
        self.first_item = True

    def close_spider(self, spider):
        self.file.write("\n]")
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(item, ensure_ascii=False)
        if self.first_item:
            self.file.write(line)
            self.first_item = False
        else:
            self.file.write(",\n" + line)
        return item

