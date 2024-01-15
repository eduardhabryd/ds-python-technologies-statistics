import scrapy
from scrapy.http import Response
from urllib.parse import urljoin
from typing import Generator, Optional, Dict


class DjinniSpiderSpider(scrapy.Spider):
    name = "djinni_spider"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(
            self, response: Response, **kwargs
    ) -> Generator[scrapy.Request, None, None]:
        for job_item in response.css(".list-jobs__item.job-list__item"):
            yield response.follow(
                urljoin(
                    response.url,
                    job_item.css(".h3.job-list-item__link::attr(href)").get()
                ),
                callback=self._parse_single_job,
            )

        number_of_pages_html = response.css(
            "ul.pagination > li:nth-last-child(2) a::text"
        ).get()
        number_of_pages = (
            int(number_of_pages_html)
            if number_of_pages_html
            else 1
        )
        current_page = 2
        while current_page <= int(number_of_pages):
            yield response.follow(
                f"https://djinni.co/jobs/"
                f"?primary_keyword=Python&page={current_page}",
                callback=self.parse,
            )
            current_page += 1

    def _parse_single_job(
            self, response: Response, **kwargs
    ) ->  Optional[Dict[str, Optional[str]]]:
        technologies = response.css(
            '.job-additional-info--item-text span[class=""]::text'
        ).getall()
        title = response.css("h1::text").get().replace('\n', ' ').strip()
        company = response.css(
            ".job-details--title::text"
        ).get().replace('\n', ' ').strip()
        yield {
            "title": title,
            "company": company,
            "link": response.url,
            "technologies": technologies,
        }
