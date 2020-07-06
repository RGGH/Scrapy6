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
from items import FoodcomItem
from scrapy import Request

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
            # follow link to details to get recipe & ingredients - pass link over as cb_kwargs? No need.
            #yield {"link" : link} # just for testing items - remove in due course.
            # UN comment
            request = Request(url=link, headers=self.headers, callback=self.parse_details)
            yield request
        # add next_page code here
        # next_page =

    def parse_details(self,response):
        print("OK")
        # get RECIPE
        # get INGREDIENTS
        # yield to items / send to FEEDS

# main driver #
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(foodcom)
    process.start()
