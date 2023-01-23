from selenium import webdriver
from badminton_doubles_adult import doubles_adult
from webdriver_manager.chrome import ChromeDriverManager

def main():
    
    activity = ""
    select = 5
    print("Which activity do you want?\n1. Badminton Family") 
    print("2. Badminton Adult \n3. Badminton All Ages\n4. Swimming" )

    while select < 0 or select > 4:
        select = int(input(""))

        if not select:
            activity = "Badminton - Family"
            break
        elif select == 1:
            activity = "Badminton doubles - adult"
            break
        elif select == 2:
            activity = "Badminton doubles - adult"
            break
        elif select == 3:
            activity = "Badminton doubles - all ages"
            break
        elif select == 4:
            activity = "Lane swim"
            break


    browser = webdriver.Chrome(ChromeDriverManager().install())
    print("to")
    print(activity)
    doubles_adult(browser, activity) 

if __name__ == "__main__":
    main()