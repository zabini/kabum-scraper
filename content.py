import requests, json
from bs4 import BeautifulSoup
from pagination import Pagination
from item import Item
from products import Products

class Content:

  pagination = None

  def __init__(self):
    self.products = Products()
    self.pagination = Pagination()
    self.item = Item()

  def handle(self, cat, link):

    self.pagination.reset()

    while True:
      soup_page = BeautifulSoup(self.req(link),'html.parser')
      if self.check_has_products(soup_page) is False:
        break

      elements = self.select_products(soup_page)

      self.handle_elements(elements)

      self.pagination.next()

    return None

  def check_has_products(self,page):

    elements = self.select_products(page)

    if len(elements) > 0:
      return True
    else:
      return False

  def req(self,link):
    url = "%s%s" % (link,str(self.pagination))
    req = requests.get(url)
    return req.text

  def select_products(self,page):
    return page.findAll("section", {"class": "listagem-box"})

  def handle_elements(self, elements):

    while len(elements) > 0:
      el = elements.pop(0)
      scraped_item = self.item.scrap(el)

      if self.products.check_in('code',scraped_item['code']) is not True:
        self.products.append(scraped_item)

    self.products.save()
