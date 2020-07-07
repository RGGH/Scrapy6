# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import scrapy


class FoodcomItem(scrapy.Item):

    recipe = scrapy.Field()
    ingredients = scrapy.Field()
    name = scrapy.Field()
