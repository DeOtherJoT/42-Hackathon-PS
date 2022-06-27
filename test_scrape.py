from bs4 import BeautifulSoup
import requests

# the link to the Lazada website.
url = "https://www.lazada.com.my/products/redmi-note-11-11s10s6gb8gb128gboriginal-xiaomi-malaysia-ready-stock-i2804862797.html"

# sends a request to get the html file using the link
data = requests.get(url).text

# makes the html file readable
soup = BeautifulSoup(data)

# looks through the html file for <h1 class="pdp-mod-product-badge-title"> and the .text takes the text within the tags
product_name = soup.find('h1', class_ = 'pdp-mod-product-badge-title').text

# same as above, but gets the price
product_price = soup.find('span', class_ = 'pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl').text

# my attempt to try and get the stock data of the product. Not perfect yet :(
# tells the program to try to look for the tag class="quantity-content-default", but in the case of 'Out of stock', this will be an error
try:
	temp = soup.find('span', class_ = 'quantity-content-default').text
# so in the case of an error {in python its called an exception, hence the keyword <except:>} it'll look for the 'Out of stock' text.
except:
	product_quantity = soup.find('span', class_ = "quality-content-warning").text
# in the case where there is a stock count, it will pass the proper message to product_quantity, i.e. 'Only x items left'
else:
	product_quantity = soup.find('span', class_ = 'quantity-content-default').text

# prints out the name, quantity and price of the product
print(product_name)
print(product_quantity)
print(product_price)
