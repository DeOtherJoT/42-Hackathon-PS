from bs4 import BeautifulSoup, SoupStrainer
import requests

url = "https://www.lazada.com.my/products/redmi-note-11-11s10s6gb8gb128gboriginal-xiaomi-malaysia-ready-stock-i2804862797.html"

data = requests.get(url).text
soup = BeautifulSoup(data)

product_name = soup.find('h1', class_ = 'pdp-mod-product-badge-title').text
product_price = soup.find('span', class_ = 'pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl').text
#temp = soup.find('span', class_ = 'quantity-content-default').text

try:
	temp = soup.find('span', class_ = 'quantity-content-default').text
except:
	product_quantity = soup.find('span', class_ = "quality-content-warning").text
else:
	product_quantity = soup.find('span', class_ = 'quantity-content-default').text

"""if temp == None:
	product_quantity = soup.find('span', class_ = "quantity-content-warning").text
else:
	product_quantity = temp.text"""

print(product_name)
print(product_quantity)
print(product_price)
