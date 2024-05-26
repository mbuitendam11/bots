from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


def sanitisePrice(item):
    i_text = item.text
    i_text = i_text.split(" - ")[1]
    if "," in i_text:
        i_text = i_text.replace(",", "")
    return i_text

def get_money() -> int:
    money = driver.find_element(By.CSS_SELECTOR, "#money").text
    if "," in money:
        money.replace(",", "")
    return int(money)

def buy_items():
    storeItems = driver.find_elements(By.CSS_SELECTOR, "#store div")
    money = get_money()
    storeItems.pop()
    for item in reversed(storeItems):
        price = sanitisePrice(item)
        print(price)
        if price <= money:
            item.click()

def click_cookie():
    driver.find_element(By.ID, "cookie").click()

buy_timer = time.time() + 5 ## Every 5 seconds
complete_timer = time.time() + 60*5 ## 5 mins from now
automate = True

while automate:
    click_cookie()
    if time.time() > buy_timer:
        try:
            buy_items()
        except:
            pass
        buy_timer = time.time() + 5

    if time.time() > complete_timer:
        print(driver.find_element(By.ID, "cps").text)
        automate = False

driver.quit()
