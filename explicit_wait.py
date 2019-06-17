from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# calculation function
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# open browser
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

# waiting until price is 10000
ifc = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,"h5#price"), "10000 RUR")
    )

button = browser.find_element_by_id("book")
button.click()

# calculaton
x_element = browser.find_element_by_css_selector('span#input_value')
x = x_element.text
y = calc(x)

# submiting the answer
input = browser.find_element_by_id('answer')
input.send_keys(y)

button = browser.find_element_by_xpath("//button[text()='Отправить']")
button.click()
