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
    nxp = 1
    # https://www.food.com/recipe/all/healthy?pn=1
    list_url = 'https://www.food.com/recipe/all/healthy?pn='
    start_urls = [list_url + str(page)]

    headers = {
                'user-agent' : "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
               }
    try:
        os.remove("foodresults.csv")
    except OSError:
        pass



    def parse(self,response):
        res = response.xpath('//script[@type="application/ld+json"]/text()').get()
        res = json.loads(res)
        #pprint(res)
        # iterate through each batch of recipes - 8 on very first 'page'
        for i in range(8):
            # print(res['itemListElement'][i]['url'])
            link = (res['itemListElement'][i]['url'])
            #yield {"link" : link }
            request = Request(url=link, headers=self.headers, callback=self.parse_details)
            yield request
        # add next_page code here
        next_page = (self.list_url+str(self.nxp+1))
        self.nxp +=1
        if response.xpath("//link/@rel='next\'").get() == "1":
            print("GET SECOND PAGE")
            yield response.follow(url=next_page,callback=self.parse)

    def parse_details(self,response):
        print("OK")
        # get RECIPE
        res = response.xpath('//script[@type="application/ld+json"]/text()').get()
        recipe = json.loads(res)
        i = 0
        # get length of recipe
        rcpl = (len(recipe['recipeInstructions']))
        ls =[]
        while i < rcpl:
            rcptx = (recipe['recipeInstructions'][i]['text'])
            ls.append(rcptx)
            i += 1
            print(ls)


        # get INGREDIENTS
        ingredients = (recipe['recipeIngredient'])

        # get RECIPE NAME
        name = (recipe['name'])

        # yield to items / send to FEEDS


        yield{'name':name,'ingredients':ingredients,'recipe':ls}

# main driver #
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(foodcom)
    process.start()
