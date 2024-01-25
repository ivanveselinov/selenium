from selenium import webdriver
import time 

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

input_element = browser.find_element("css selector", 'input[id="ipt1"]')
input_element.send_keys("test")

button_click = browser.find_element("css selector", 'button[id="b1"]')
button_click.click()

time.sleep(5)

browser.quit()