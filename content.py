from pagination import Pagination

class Content:

  pagination = None

  def __init__(self):
    self.pagination = Pagination()

  def handle(self, cat, link):

    self.pagination.reset()

    print(self.pagination)
    print(cat,link,sep='|')
    print('\n\n')

    self.req(link)

    return None

  def check_has_elements(self):
    pass

  def req(self,link):

    a = "%s%s" % (link,str(self.pagination))
    print(a)
