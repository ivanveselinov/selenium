from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

# Find elements ID or identifications
input2_css_locator = "input[id='ipt2']"
button4_xpath_locator = "//button[@id='b4']"

# Assign elements
input2_elem = browser.find_element("css selector", input2_css_locator)
butn4_elem = browser.find_element("xpath", button4_xpath_locator)

# Manipulate elements
input2_elem.send_keys("Test text")

time.sleep(5)

butn4_elem.click()

time.sleep(2)

browser.quit()



