# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def strip(value):
    if isinstance(value, str):
        v = value.replace('\r', '')
        v = v.replace('\n', '')
        v.strip()
        return v


def remove_go_to(value: str):
    return value.replace('Go to: ', '')


class TorLinksItem(scrapy.Item):
    site_name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst())
    description = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip),
        output_processor=TakeFirst())
    link = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_go_to),
        output_processor=TakeFirst())
    likes = scrapy.Field(
        serializer=int,
        input_processor=MapCompose(remove_tags, strip),
        output_processor=TakeFirst())
    dislikes = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip),
        output_processor=TakeFirst())
