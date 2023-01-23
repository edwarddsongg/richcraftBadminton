from selenium import webdriver
import time
import urllib
import urllib.request
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common import exceptions

def find_date(class_name, browser):
    dates = browser.find_elements(By.CLASS_NAME, class_name)
    available = len(dates)

    week_dates = browser.find_elements(By.CLASS_NAME, "title")
    print(len(week_dates))
    if not len(week_dates):
        print("There are no times this week")
        return
    else:
        print("why")
        for date in week_dates:
            date.click()

    time.sleep(1)

    reservation_count = browser.find_element(By.ID, "reservationCount")
    reservation_count.clear()
    reservation_count.send_keys(2)

    button = browser.find_element(By.ID, "submit-btn")
    button.click()

    if not available:
        print("There are no more available dates")
    else:
        for d in dates:
            d.click()
            times = browser.find_elements(By.CLASS_NAME, "mdc-button")
            
            print("times:")
            print(len(times))
            
            for t in times:
                t.click()
                
                phone_number = browser.find_element(By.ID, "telephone")
                phone_number.send_keys("6136681312")
               
                email = browser.find_element(By.ID, "email")
                email.send_keys("edwardsongg@gmail.com")
                name = browser.find_element(By.ID, "field2021")
                name.send_keys("Edward Song")

                browser.find_element(By.ID, "submit-btn").click()
                break

            break
        
            cur_link = browser.current_url

    
def doubles_adult(browser, activity):
    dateTime = time.strftime("%H:%M")

    link = "https://reservation.frontdesksuite.ca/rcfs/richcraftkanata/Home/Index?Culture=en&PageId=b3b9b36f-8401-466d-b4c4-19eb5547b43a&ShouldStartReserveTimeFlow=False&ButtonId=00000000-0000-0000-0000-000000000000"
    refreshRate = 1
    
    browser.get(link)

    button = browser.find_element(By.LINK_TEXT, activity)
    button.click()
    time.sleep(1)
   
    find_date("date-text", browser)

    time.sleep(20)

