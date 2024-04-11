from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

browser = webdriver.Chrome()

alert = Alert(browser)


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://techstepacademy.com/training-ground"


    def go(self):
        self.driver.get(self.url)

    def type_input_field(self, text):
        input = self.driver.find_element("xpath", '//*[@id="ipt1"]')
        input.clear()
        input.send_keys(text)
        time.sleep(2)
        return None

    def get_input_text(self):
        input = self.driver.find_element("xpath", '//*[@id="ipt1"]')
        elem_text = input.get_attribute('value')
        return elem_text

    def click_button_1(self):
        button = self.driver.find_element("xpath", '//*[@id="b1"]')
        button.click()
        time.sleep(2)
        alert.accept()
        return None

# Test
test_value = 'It Worked!'
training_page = TrainingGroundPage(driver=browser)
training_page.go()
training_page.type_input_field(test_value)
training_page.click_button_1()
txt_from_input = training_page.get_input_text()

assert txt_from_input == test_value, f"Test Failed: Input did not match expected value : {test_value}"
print('Test Passed.')


