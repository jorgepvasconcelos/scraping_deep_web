from pathlib import Path


import scrapy


class LinkListSpider(scrapy.Spider):
    name = "link_list"
    allowed_domains = ["lll6kral3vyokwz7m7ce5smuk55bgj75l2gev3zzqkifn7f7hpj2auid.onion"]

    def start_requests(self):
        urls = ["http://lll6kral3vyokwz7m7ce5smuk55bgj75l2gev3zzqkifn7f7hpj2auid.onion/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
