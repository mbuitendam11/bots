from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
ITEM_PRICE = 99 ##original price

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

r = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(r.content, "lxml")

current_price = soup.find(class_="a-price-whole").getText().split(".")[0] ## Finds price, gets the text then turns splits into an array and returns the first item

if int(current_price) < ITEM_PRICE:
    print("its currently on sale")
else:
    print("no sales on at the moment.")
