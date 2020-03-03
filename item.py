import re

class Item:

  def scrap(self,soup_item,cat):

    img_div = soup_item.find('div', {'class': 'listagem-img'})
    img_a = img_div.find('a')
    img_el = img_div.find('img')

    fab = soup_item.find('li',{'class': 'imagem-fabricante'})
    fab = fab.find('img')

    cash_price = self.price_handle(soup_item,'div','listagem-precoavista')
    price = self.price_handle(soup_item,'div','listagem-preco')
    mkt_place_low_price = self.price_handle(soup_item,'b','mktplace_preco_menor')

    stars = soup_item.find('div',{'class': 'H-estrelas'})
    stars = stars.attrs['class'][1].replace('e','')
    stars = int(stars) if stars != '' else 0

    rating = soup_item.find('li',{'class': 'notas'})
    rating = rating.text.strip()

    link = soup_item.find('h2',{'class':'H-titulo'}).find('a')

    evaluation = 0
    if rating != '':
      rgx = re.search("[0-9]+", rating)
      evaluation = int(rating[rgx.start():rgx.end()])

    el = {
      'code': int(img_a.attrs['data-id']), # Item code
      'title': img_el.attrs['alt'], # Item Title,
      'category': cat ,
      'img_src': img_el.attrs['src'], # Item img src
      'link': link.attrs['href'], # Item link
      'maker': fab.attrs['alt'].replace('Logo ',''), # Item maker
      'evaluation': evaluation, # Item Evaluation
      'star': stars, # Item stars
      'price': price, # Cash price
      'cash_price': cash_price, # Cash price
      'mkt_place_low_price': mkt_place_low_price, # Cash price
    }

    return el

  def price_handle(self, soup_item, tag, class_name):
    price_el = soup_item.find(tag,{'class': class_name})

    if price_el is not None:
      price = price_el.text
      price = re.sub("(R\$)|(\.)|(\,)",'',price).strip()
      price = float(price[:-2] + '.' + price[-2:])
    else:
      price = 0.0

    return price
