from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import os
import math
def matt(x):
        return str(math.log(abs(12 * math.sin(x))))
try:
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get(link)
        price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
        button = browser.find_element(By.ID, "book")
        button.click()
        butt = browser.find_element(By.ID, "input_value")
        browser.execute_script("return arguments[0].scrollIntoView(true);", butt)
        input1 = browser.find_element(By.ID, "input_value")
        answer = matt(int(input1.text))
        input2 = browser.find_element(By.ID, "answer")
        input2.send_keys(answer)
        button1 = browser.find_element(By.ID, "solve")
        button1.click()

finally:
        time.sleep(30)
        browser.quit()