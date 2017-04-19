# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pegasimporter.items import PegasimporterItem
from scrapy.spiders import CSVFeedSpider
import string 


class TestSpider(CrawlSpider):
    name = 'jb'
    allowed_domains = ['jobandtalent.com']
    delimiter = ';'
    start_urls = ['http://www.jobandtalent.com/cl/ofertas-de-empleo?page=%s' % page for page in xrange(1,500)]

    rules = (
        Rule(LinkExtractor(allow='/cl/ofertas-de-empleo/\w*'), callback='parse_item'),
    )



    def parse_item(self, response):
        
        item = PegasimporterItem()
        item['cargo'] = map(unicode.strip, response.xpath('//*//*[@id="cand_job_page"]/div[1]/div[2]/h1/text()').extract())
        item['empresa'] = map(unicode.strip, response.xpath('//*/span[@data-where="job_opening_company_name"]/text()').extract()) #span data-where="job_opening_company_name"
        item['link'] = response.url
        item['ciudad'] = map(unicode.strip, response.xpath('//*[@id="cand_job_header"]/div/h1/span/a[2]/text()').extract())
        item['fpublicacion'] = response.xpath('normalize-space(//*[@id="cand_job_page"]/div[2]/ul/li[1])').extract()
         

        yield item 
