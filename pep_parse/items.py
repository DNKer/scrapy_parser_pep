import scrapy


class PepParseItem(scrapy.Item):
    """Определяет поля элементов (items) парсера."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
