from bs4 import BeautifulSoup as soup
from urllib import urlopen as uReq

my_url = "http://www.billboard.com/charts/hot-100"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"chart-row__title"})

file_name = "songs.csv"
f = open(file_name, "w")

Headers = "SONG NAME, ARTIST \n"

f.write(Headers)



for song in containers :

    song_name = song.findAll("h2", {"class": "chart-row__song"})

    track = song_name[0].text.strip()
    print(track)

    artist_name = song.findAll("a", {"class": "chart-row__artist"}) or song.findAll("span", {"class":"chart-row__artist"})
    singer = artist_name[0].text.strip()
    print(singer)

    f.write(str(track.replace(",", "|")) + ',' + str(singer.replace(",", "|") + '\n'))
    











