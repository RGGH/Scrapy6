# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import os
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader

class foodcom(scrapy.Spider):

    name = 'food-com'
    custom_settings = {"FEEDS": {"foodresults.csv":{"format":"csv"}}}
    start_urls = ['https://www.food.com/recipe/all/healthy']
    headers = {
                'user-agent' : "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
               }
    try:
        os.remove("foodresults.csv")
    except OSError:
        pass


    def parse(self,response):
        pass
        # iterate through each batch of recipes - 10 on very first 'page'
        #
        # add next_page code here
        #

    def parse_details(self,response):
        pass
        # get recipe and ingredients and yield to items / send to FEEDS

# main driver #
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(foodcom)
    process.start()
