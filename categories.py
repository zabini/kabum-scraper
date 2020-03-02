import os, json
from content import Content

class Categories:

  env_path = 'categories_path'
  data = None

  def __init__(self):
    self.read()
    self.content = Content()

  def read(self):

    path = os.getenv(self.env_path)

    if os.path.isfile(path) is not True:
      self.data = []
    else:
      with open(path) as json_file:
        self.data = json.load(json_file)

  def iterate(self):

    for el in self.data:
      rs_handle = self.content.handle(el['desc'],el['link'])
