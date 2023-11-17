import scrapy


class DjinniSpiderSpider(scrapy.Spider):
    name = "djinni_spider"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response):
        pass
