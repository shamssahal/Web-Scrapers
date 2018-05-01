from bs4 import BeautifulSoup as soup
from urllib import urlopen as uReq

my_url = "https://imgur.com/gallery/D0WYr"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "post-image"})

x = 0

for memes in containers:
    x += 1
    meme = "https:"+memes.a.img['src']
    print meme
    file_name = "meme"+str(x)+".png"
    image_file = open(file_name, "wb")
    image_file.write(uReq(meme).read())
    image_file.close()












