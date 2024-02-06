from selenium import webdriver
from selenium.webdriver.support.select import Select 
import time

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/training-ground")

sel = browser.find_element("css selector", 'select[id="sel1"]')
# sel.click()
my_select = Select(sel)

# Select element from dropdown!!
# my_select.select_by_visible_text('Battlestar Galactica')

# Select element by Index!!
# my_select.select_by_index(1)

# Select element by Value
my_select.select_by_value('third')

# Select element by first selected option 
option = my_select.first_selected_option
option.text
print(option.text)

time.sleep(5)
