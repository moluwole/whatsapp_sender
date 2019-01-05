import sys
from selenium import webdriver  # Selenium Driver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import FirefoxDriverManager


WHATSAPP_URL = "https://web.whatsapp.com"

def main(string_message, number):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(WHATSAPP_URL)
    wait = WebDriverWait(driver, 300)

    new_chat = '//*[@id="side"]/div[1]/div/label/input'

    x_arg = "//*[contains(@title,'" + number + "')]"
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()

    # group_title.find_elements_by_xpath('//span[contains(@title,')

    # xpath = '//*[@id="pane-side"]/div/div/div/div[14]/div/div/div[2]/div[1]/div[1]/span/span'

    # input_box = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

    # input_box.send_keys(string_message)

    # sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    # sendbutton.click()

    # driver.close()


    # inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'

    input_box = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    input_box.send_keys(string_message + Keys.ENTER)

    # for i in range(100):
    #     input_box.send_keys(string_message + Keys.ENTER)
    #     time.sleep(1)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2]) #Argument passing via CMD
