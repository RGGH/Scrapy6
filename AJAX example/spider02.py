# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import os
import json
from pprint import pprint
import urllib.parse
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader

class foodcom(scrapy.Spider):

    name = 'food-com'
    custom_settings = {"FEEDS": {"foodresults.csv":{"format":"csv"}}}

    page = 1
    start_urls = ['https://www.food.com/recipe/all/healthy?pn=' + str(page)]

    headers = {
                'user-agent' : "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
               }
    try:
        os.remove("foodresults.csv")
    except OSError:
        pass



    def parse(self,response):
        # iterate through each batch of recipes - 8 on very first 'page'
        res = response.xpath('//script[@type="application/ld+json"]/text()').get()
        res = json.loads(res)
        for i in range (8):
            link = (res['itemListElement'][i]['url'])
            print(link)
        #
        # add next_page code here
        # next_page =

    def parse_details(self,response):
        pass
        # get recipe and ingredients and yield to items / send to FEEDS

# main driver #
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(foodcom)
    process.start()
