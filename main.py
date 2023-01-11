from selenium import webdriver
import time
import urllib
import urllib.request
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

dateTime = time.strftime("%H:%M")

link = "https://ottawa.ca/en/recreation-and-parks/recreation-facilities/facility-listing/richcraft-recreation-complex-kanata"
refreshRate = 1
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(link)

while dateTime != dateTime:
    print(dateTime)
    time.sleep(refreshRate)
    browser.refresh()

button = browser.find_element(By.XPATH, "//button[contains(text(),'racquet sports')]")
button.click()
time.sleep(2)
reserve =  browser.find_element(By.XPATH, "//div[@class='paragraph paragraph--type--text-block paragraph--view-mode--default']/div[@class='clearfix text-formatted field field--name-field-body field--type-text-long field--label-hidden field__item']/p/a")
time.sleep(5)

browser.quit()