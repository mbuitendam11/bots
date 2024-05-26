from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")


eventDate = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
eventName = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

event = {}

for n in range(len(eventDate)):
    event[n] = {
        "Time": eventDate[n].text,
        "name": eventName[n].text
    }
print(event)

# driver.close()
driver.quit()