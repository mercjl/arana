# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PegasimporterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cargo = scrapy.Field()
    empresa = scrapy.Field()
    link = scrapy.Field()
    ciudad = scrapy.Field()
    fpublicacion = scrapy.Field()