import sys, requests, json, logging, time
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

  def handle(self,cat,link):

    self.pagination.reset()

    while True:

      logging.info( 'Scraping [%s] page, checking products.' % str(self.pagination.actual))

      soup_page = BeautifulSoup(self.req(link),'html.parser')
      if self.check_has_products(soup_page) is False:
        logging.info( 'No more products found in this category, going to next.')
        break

      elements = self.select_products(soup_page)

      logging.info( 'More products founded on page [%s], scraping them.' % str(self.pagination.actual))
      logging.info( 'Total products [%s].' % str(len(elements)))

      self.handle_elements(elements, cat)

      self.pagination.next()
      time.sleep(1)

  def check_has_products(self,page):

    elements = self.select_products(page)

    if len(elements) > 0:
      return True
    else:
      return False

  def req(self,link):

    url = "%s%s" % (link,str(self.pagination))

    try:
      req = requests.get(url,timeout=10)
      req.raise_for_status()
      return req.text
    except requests.exceptions.Timeout as Timeout:
      logging.info('Timeout exception, sleeping and repeat...')
      time.sleep(30)
      return self.req(link)
    except requests.exceptions.RequestException as RequestException:
      logging.info('A Request exception ocurred, ending scraping. [status_code=%s]' % req.status_code)
      time.sleep(30)
      return self.req(link)

  def select_products(self,page):
    return page.findAll("section", {"class": "listagem-box"})

  def handle_elements(self,elements,cat):

    while len(elements) > 0:
      el = elements.pop(0)
      scraped_item = self.item.scrap(el,cat)

      if self.products.check_in('code',scraped_item['code']) is not True:
        self.products.append(scraped_item)

    self.products.save()
