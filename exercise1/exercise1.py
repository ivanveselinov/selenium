from selenium import webdriver
import time

browser = webdriver.Chrome()

# Navigate to the webpage
browser.get("https://techstepacademy.com/training-ground")

# Find the input element using CSS selector by ID
input_element = browser.find_element("css selector", 'input[id="ipt1"]')

# Insert text into input field
input_element.send_keys("My first Automation!!")
 
# Find the button using CSS selector by Name
button_element = browser.find_element("css selector", 'button[name="butn1"]')

time.sleep(2)

# Click the button
button_element.click()

# Sleep for 5 sec
time.sleep(5)

# Close the browser
browser.quit()