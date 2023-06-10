# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HoopshypeScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# We're defining a new class, which we'll use to structure the data we're scraping
class PlayerItem(scrapy.Item):
    # These are the fields we'll be scraping. Each field is defined as a scrapy.Field()
    # The actual keys used for scraped data will be the variable names here - 'Player', 'Salary', 'Year', 'Link', 'Born'
    Player = scrapy.Field()
    Salary = scrapy.Field()
    Year = scrapy.Field()
    Link = scrapy.Field()
    Born = scrapy.Field()
