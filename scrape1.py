from bs4 import BeautifulSoup as soup
from urllib import urlopen as uReq
import re

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()


page_soup = soup(page_html, "html.parser")
# print(page_soup.p)
# print(page_soup.h1)

containers = page_soup.findAll("div",{"class":"item-container"})#all 12 items

filename = "products.csv"
f = open(filename, "w")

Headers = "BRAND, MODEL,PRICE, SHIPPING \n"
f.write(Headers)

for product in containers:

    brand = (product.div.div.a.img["title"])
    print(brand)

    name_of_product = product.findAll("a", {"class": "item-title"})
    model = name_of_product[0].text
    print(model)

    price_of_product = product.findAll("li", {"class": "price-current"})
    price = (re.findall(r'\$\d*\.\d{2}', price_of_product[0].text.strip()))
    curr_price = price[0]
    print(curr_price)

    shipping_details = product.findAll("li", {"class": "price-ship"})
    ship_price = shipping_details[0].text.strip()
    print(ship_price)

    f.write(str(brand)+","+str(model.replace(",", "|"))+","+str(curr_price)+","+str(ship_price) + "\n")
