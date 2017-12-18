# -*- coding: utf-8 -*-
import scrapy


class NewsScrapingSpider(scrapy.Spider):
    name = 'news_scraping'
    allowed_domains = ['www.cnbc.com/world/?region=world']
    start_urls = ['https://www.cnbc.com/world/?region=world/']

    def parse(self, response):

        container1 = response.xpath('//*[@class="featured_secondary"]//*[@class="headline"]')
        for each in container1:
            tittle = each.xpath('.//a/text()').extract_first().strip()
            temp_url = each.xpath('.//a/@href').extract_first()
            url = response.urljoin(temp_url)
            yield {'Tittle':tittle,'URL':url}

        container2 = response.xpath('//*[@id="pipeline_assetlist_1"]//*[@class="headline"]')
        for each in container2:
            tittle = each.xpath('.//a/text()').extract_first()
            if not tittle:          #Tittle may be null
            	continue
            tittle = tittle.strip()
            temp_url = each.xpath('.//a/@href').extract_first()
            url = response.urljoin(temp_url)
            yield {'Tittle':tittle,'URL':url}

        	
