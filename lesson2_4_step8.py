from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

browser.execute_script("window.scrollBy(0, 100);")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(y)

button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(10)
browser.quit()

