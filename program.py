import random
from random import randint
import requests
import csv
from bs4 import BeautifulSoup
from time import sleep

# class for Lazada Items
class	LazadaItems:
	def __init__(self, n, p, q):
		self.name = n
		self.price = p
		self.quantity = q
	
	def	LZ_name_get(self):
		return (self.name)
	
	def	LZ_price_get(self):
		return (self.price)

	def	LZ_quantity_get(self):
		return (self.quantity)
	
	def	LZ_print_all(self):
		print("Name : " + self.name + " , Price : " + self.price + " , Quantity : " + self.quantity)

# get an array of available proxies for proxy rotation
def generate_proxyList(file):
	proxyList = []
	with open(file, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			proxyList.append(row[0])
	return (proxyList)

def	get_urlList(file):
	urlList = []
	with open(file, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			urlList.append(row[0])
	return (urlList)

# get a random proxy from the array of proxies.
def	get_proxyVal(proxyList):
	return (random.choice(proxyList))

LazadaProducts = []
proxyList = generate_proxyList('Attempt\proxylist.txt')
# proxy = get_proxyVal(proxyList)

url = get_urlList('Attempt\Data for 42KL Hackathon - Lazada Links .csv')

i = 0
while i < 5:
	proxy = get_proxyVal(proxyList)
	data = requests.get(url[randint(0,60)], proxies={"http": proxy, "https": proxy}).text
	soup = BeautifulSoup(data, 'html.parser')

	product_name = soup.find('h1', class_ = 'pdp-mod-product-badge-title').contents[0]
	product_quantity = soup.find('div', class_='pdp-mod-product-info-section sku-quantity-selection').find_all('span')[-1].text
	product_price = soup.find('span', class_ = 'pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl').contents[0]

	LazadaProducts.append(LazadaItems(product_name, product_price, product_quantity))
	sleep(randint(2, 10))
	i += 1

# print (len(LazadaProducts))

for x in LazadaProducts:
	x.LZ_print_all()