from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Mathew")
lName = driver.find_element(By.NAME, "lName")
lName.send_keys("Smith")
email = driver.find_element(By.NAME, "email")
email.send_keys("Something@gmail.com", Keys.ENTER)


# driver.close()
# driver.quit()