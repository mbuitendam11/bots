from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

article_tag = soup.findAll(name="a")

articleText = []
articleLink = []

for i in article_tag:
    articleText.append(i.getText())
    articleLink.append(i.get("href"))

print(articleText[:3])