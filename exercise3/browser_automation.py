from selenium import webdriver
from selenium.webdriver.support.select import Select 
import time

browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()

browser1.get("https://techstepacademy.com/training-ground")
# browser2.get("https://google.com")

browser1.execute_script('window.open("https://techstepacademy.com/training-ground", "_blank");')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground", "_blank");')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground", "_blank");')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground", "_blank");')

time.sleep(5)


# Try this in terminal !!!!

# Type python -i browser_automation.py 
# handles=browser1.window_handles
# len(handles)
# browser1.switch_to.window(handles[4])
# browser1.switch_to.window(handles[3])
# browser1.switch_to.window(handles[2])
# browser1.switch_to.window(handles[1])
# browser1.switch_to.window(handles[0])
