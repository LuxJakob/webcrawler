from scrapy.item import Item, Field


class PrototypeItem(Item):
    title = Field()
    category = Field()
    description = Field()
    price = Field()
