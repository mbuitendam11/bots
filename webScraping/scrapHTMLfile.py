from bs4 import BeautifulSoup

## Parsing through a file
file = open("website.html", encoding="utf8")
contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

allAnchors = soup.findAll(name="a")

for tag in allAnchors:
    print(tag.get("href"))

