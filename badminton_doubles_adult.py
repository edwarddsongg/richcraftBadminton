from selenium import webdriver
import time
import urllib
import urllib.request
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def doubles_adult(browser):
    dateTime = time.strftime("%H:%M")

    link = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata/Home/Index?Culture=en&PageId=b3b9b36f-8401-466d-b4c4-19eb5547b43a&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
    refreshRate = 1
    
    browser.get(link)

    button = browser.find_element(By.LINK_TEXT, "Badminton doubles - adult")
    button.click()
    time.sleep(1)

    reservation_count = browser.find_element(By.ID, "reservationCount")
    reservation_count.clear()
    reservation_count.send_keys(2)

    button = browser.find_element(By.ID, "submit-btn")
    button.click()

    time.sleep(5)

    browser.quit()