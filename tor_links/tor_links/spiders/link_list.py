from pathlib import Path

import scrapy
from itemloaders import ItemLoader

from tor_links.items import TorLinksItem


class LinkListSpider(scrapy.Spider):
    name = "link_list"
    allowed_domains = ["lll6kral3vyokwz7m7ce5smuk55bgj75l2gev3zzqkifn7f7hpj2auid.onion"]

    def start_requests(self):
        urls = ["http://lll6kral3vyokwz7m7ce5smuk55bgj75l2gev3zzqkifn7f7hpj2auid.onion/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, )

    def parse(self, response):
        for site in response.css('div[class="card m-1"]'):
            i = ItemLoader(item=TorLinksItem(), selector=site)

            i.add_css("site_name", '.justify-content-between:nth-child(1)>h4:nth-child(1)::text')
            i.add_css("description", '.justify-content-between:nth-child(2)>p:nth-child(1)::text')
            i.add_css("link", '[class="card-link stretched-link"]::text')
            i.add_css("likes", '[class="btn btn-sm btn-success"]::text')
            i.add_css("dislikes", '[class="btn btn-sm btn-danger"]::text')

            yield i.load_item()
