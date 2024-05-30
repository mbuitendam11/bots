from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests, time

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
webPage = response.text

soup = BeautifulSoup(webPage, "html.parser")


## Finding all links
# Fast way of doing it
links = [link["href"] for link in soup.findAll("a", {"class": "StyledPropertyCardDataArea-anchor"})]

# Long way of doing it
"""links = soup.findAll("a", {"class": "StyledPropertyCardDataArea-anchor"})

linkList = []

for i in links:
    linkList.append(i["href"])"""

## Finding all prices
prices = [price.text[:6] for price in soup.findAll("span", {"class": "PropertyCardWrapper__StyledPriceLine"})]

## Finding all addresses
addresses = [address.text.strip() for address in soup.findAll("address")]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


for n in range(len(links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSclzndYi3AOhXE3Z6oR6oHHx6Z5q5v52Gs9QIgwxkI6uVatHg/viewform?usp=sf_link")
    time.sleep(2)

    location = driver.find_element(By.XPATH,
                                   value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price = driver.find_element(By.XPATH,
                                   value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link = driver.find_element(By.XPATH,
                                   value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    location.send_keys(addresses[n])
    price.send_keys(prices[n])
    link.send_keys(links[n])
    submit.click()

driver.close()