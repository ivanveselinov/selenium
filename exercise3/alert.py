from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

alert = Alert(browser)

button_click = browser.find_element("css selector", 'button[id="b1"]')
button_click.click()

time.sleep(3)

# Accept alert !!!
alert.accept()

time.sleep(5)