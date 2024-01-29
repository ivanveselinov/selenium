from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/trial-of-the-stones")

# Find elements ID 
input1_element_path = 'input[id="r1Input"]'
input2_element_path = 'input[id="r2Input"]'
input3_element_path = 'input[id="r3Input"]'
button_answer1_path = 'button[id="r1Btn"]'
button_answer2_path = 'button[id="r2Butn"]'
button_answer3_path= 'button[id="r3Butn"]'
merchant_name_path = '//b[text()="Jessica"]'
submit_answer_path = 'button[id="checkButn"]'


# Assign elements and manipylate with keys
input1_element = browser.find_element("css selector", input1_element_path)
input1_element.send_keys("Rock")

button_answer1 = browser.find_element("css selector", button_answer1_path)
button_answer1.click()

input2_element = browser.find_element("css selector", input2_element_path)
input2_element.send_keys('bamboo')

button_answer2 = browser.find_element("css selector", button_answer2_path) 
button_answer2.click()

input3_element = browser.find_element("css selector", input3_element_path)
merchant_name = browser.find_element("xpath", merchant_name_path)
merchant_name_attribute = merchant_name.get_attribute('innerHTML')
input3_element.send_keys(merchant_name_attribute)

button_answer3 = browser.find_element("css selector", button_answer3_path)
button_answer3.click()

submit_answer = browser.find_element("css selector", submit_answer_path)
submit_answer.click()


time.sleep(10)

browser.quit()