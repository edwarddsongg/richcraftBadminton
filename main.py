from selenium import webdriver
from badminton_doubles_adult import doubles_adult
from webdriver_manager.chrome import ChromeDriverManager

def main():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    print("yp")
    doubles_adult(browser)

if __name__ == "__main__":
    main()