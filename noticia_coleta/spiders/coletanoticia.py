# -*- coding: utf-8 -*-
import scrapy


class ColetanoticiaSpider(scrapy.Spider):
    name = 'coletanoticia'
    allowed_domains = ['https://www1.folha.uol.com.br/ultimas-noticias/#10']
    start_urls = ['http://https://www1.folha.uol.com.br/ultimas-noticias/#10/']

    def parse(self, response):
        pass
