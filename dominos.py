from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

def pizza():
    edge_driver_location = "C:\Drivers\Edge Driver\msedgedriver.exe"
    driver = webdriver.Edge()

    driver.maximize_window()
    driver.get("https://pizzaonline.dominos.co.in/")
    sleep(10)

    # speak("Getting Ready To Order")
    search_box = driver.find_element(By.CLASS_NAME, "srch-cnt-srch-inpt")
    search_box.click()
    sleep(2)

   # speak("Entering Your Location")
    location = "Amritsar Bus Stand Mehar Pura"

    location_box = driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input'
    )
    location_box.send_keys(location)
    sleep(2)

    location_select = driver.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div[2]/span[2]'
    )
    location_select.click()
    sleep(2)

    try:
        login = driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]'
        )
        login.click()
        sleep(2)
    except:
        # speak("your location is not found")
        exit()

        # speak("Logging In")

        phone_num = "1234567890"
        login_details = driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input'
        )
        login_details.send_keys(phone_num)
        sleep(2)

        submit_login_btn = driver.find_element(
            By.XPATH, '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input'
        )
        submit_login_btn.click()
pizza()