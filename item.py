import re

class Item:

  def scrap(self,soup_item):

    img_div = soup_item.find('div', {'class': 'listagem-img'})
    img_a = img_div.find('a')
    img_el = img_div.find('img')

    fab = soup_item.find('li',{'class': 'imagem-fabricante'})
    fab = fab.find('img')

    cash_price = soup_item.find('div',{'class': 'listagem-precoavista'}).text
    cash_price = re.sub("(R\$)|(\.)|(\,)",'',cash_price).strip()
    cash_price = float(cash_price[:-2] + '.' + cash_price[-2:])

    price_el = soup_item.find('div',{'class': 'listagem-preco'})

    if price_el is not None:
      price = price_el.text
      price = re.sub("(R\$)|(\.)|(\,)",'',price).strip()
      price = float(price[:-2] + '.' + price[-2:])
    else:
      price = 0.0

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
      'img_src': img_el.attrs['src'], # Item img src
      'link': link.attrs['href'], # Item link
      'maker': fab.attrs['alt'].replace('Logo ',''), # Item maker
      'evaluation': evaluation, # Item Evaluation
      'star': stars, # Item stars
      'price': price, # Cash price
      'cash_price': cash_price, # Cash price
    }

    return el
