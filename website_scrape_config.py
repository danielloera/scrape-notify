import re

class WebsiteScrapeConfig:

    def __init__(self, url=None, wait_for_class= None, item_class=None):
        self.url = url
        self.wait_for_class = wait_for_class
        self.item_class = item_class