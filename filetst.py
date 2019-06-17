from selenium import webdriver
import os 

# open browser
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

#filling inputs
input1 = browser.find_element_by_name('firstname')
input1.send_keys("Ivan")

input2 = browser.find_element_by_name('lastname')
input2.send_keys("Petrov")

input3 = browser.find_element_by_name('email')
input3.send_keys("I.P@ml.com")

# getting path from current file
current_dir = os.path.abspath(os.path.dirname('filetst.py'))    
# adding file name to path
file_path = os.path.join(current_dir, 'file.txt')           

# attaching file
chk = browser.find_element_by_css_selector('input#file')
chk.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()
