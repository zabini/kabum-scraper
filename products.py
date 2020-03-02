import os, json

class Products:

  env_path = 'products_path'
  data = None

  def __init__(self):
    self.read()

  def read(self):

    path = os.getenv(self.env_path)

    if os.path.isfile(path) is not True:
      self.data = []
    else:
      with open(path) as json_file:
        self.data = json.load(json_file)

  def append(self, reg):
    self.data.append(reg)

  def check_in(self,key,code):
    if code in [ el[key] for el in self.data ]:
      return True
    else:
      return False

  def save(self):
    path = os.getenv(self.env_path)
    with open(path, 'w') as outfile:
      json.dump(self.data, outfile,ensure_ascii=False, indent=2)
