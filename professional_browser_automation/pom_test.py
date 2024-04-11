from selenium import webdriver

from pages.training_ground_page import TrainingGroundPage

# Test Setup

browser = webdriver.Chrome()
test_value = 'It worked!'

# Test

test_ground_page = TrainingGroundPage(driver = browser)
test_ground_page.go()
assert test_ground_page.button1.text == 'Button1'
browser.quit()