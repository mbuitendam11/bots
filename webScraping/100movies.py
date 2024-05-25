from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titles = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__BfenH")

titleList = []


for i in titles:
    titleList.append(i.getText())

with open("100MoviesToWatch.txt", "a") as file:
    for x in reversed(titleList):
        file.write(x + "\n")