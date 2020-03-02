
class Pagination:

  actual = None
  page_str = None

  def __init__(self):
    self.reset()

  def __str__(self):
    return self.page_str

  def reset(self):
    self.actual = 30
    self.build(self.actual)

  def build(self,page):
    self.page_str = '?string=&pagina=%s&ordem=5&limite=100' % str(page)

  def next(self):
    self.actual = self.actual+1
    self.build(self.actual)

  def prev(self):
    self.actual = self.actual-1
    self.build(self.actual)
