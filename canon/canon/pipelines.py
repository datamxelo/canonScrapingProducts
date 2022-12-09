# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import pygsheets



class CanonPipeline:

    def process_item(self, item, spider):

        
        #1. authorization
      
        gc = pygsheets.authorize(service_file='/Users/arturoisraelperezvargas/Documents/Elogia/CrawlCanon/canon/canon-370922-d88fad5fa75a.json')
        #2.Create a datafram

        df = pd.DataFrame([item])

        # 3. Open spredhseet by link
        sh = gc.open('Feed_CANON')

        #4 Open worksheet
        wk1 = sh[1]
        
        values = [item['url'], item['avilability'], item['price']]

        counter = 1
        wk1.insert_rows(1,number = 1, values = values )#Inserts df in worksheet starting from A9
        # Note: set copy_head =False  if you don't want to add first row of df
        
        return item
