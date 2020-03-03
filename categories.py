import os, requests, json, logging
from content import Content
from bs4 import BeautifulSoup

class Categories:

  base_url = None
  env_path = 'categories_path'
  data = None

  def __init__(self):
    self.base_url = os.getenv('base_url')
    self.read()
    self.content = Content()

  def read(self):

    self.data = []

    source = self.request()

    soup = BeautifulSoup(source,'html.parser')
    menu = soup.findAll('ul',{'class': {'greybox'}})

    for ul in menu:
      lis = ul.findAll('li')
      for li in lis:
        a = li.find('a')
        url = a.attrs['href']
        cats = url.replace(self.base_url,'').split('/')
        self.data.append({'desc': cats,'link': url})

    path = os.getenv(self.env_path)

    with open(path,'w') as outfile:
      json.dump(self.data, outfile,ensure_ascii=False, indent=2)

  def iterate(self):

    for el in self.data:
      logging.info('Handling [%s] - base link [%s]' % (','.join(el['desc']).center(17),el['link']) )
      self.content.handle(el['desc'],el['link'])

  def request(self):
    req = requests.get(self.base_url)
    return req.text
