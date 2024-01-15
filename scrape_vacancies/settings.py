BOT_NAME = "scrape_vacancies"

SPIDER_MODULES = ["scrape_vacancies.spiders"]
NEWSPIDER_MODULE = "scrape_vacancies.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
