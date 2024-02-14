from selenium import webdriver
import time

aboutUs = '/html/body/div[1]/div/div[3]'
team_assurance = '/html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div/a/p'
dek_tech = '/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div/a/p'
iceConcrete = '/html/body/div[1]/div/div[5]/div/div/div[1]/a/div'
shareMemory = '/html/body/div[1]/div/div[5]/div/div/div[2]/a/div'
mls = '/html/body/div[1]/div/div[5]/div/div/div[3]/a/div'
uniquee = '/html/body/div[1]/div/div[5]/div/div/div[4]/a/div'
westernSuburb = '/html/body/div[1]/div/div[5]/div/div/div[5]/a/div'
ticTacToe = '/html/body/div[1]/div/div[5]/div/div/div[6]/a/div'
technicalSkills = '/html/body/div[1]/div/div[6]/div/div'
techicalSkillsIcons = '/html/body/div[1]/div/div[6]/div/div/div/div[7]'
educationSection = '/html/body/div[1]/div/div[7]/div/div/div[3]'
publicationSection = '/html/body/div[1]/div/div[7]/div/div/div[5]'
emailNameInput = '/html/body/div[1]/div/div[8]/div[1]/div/form/div[2]/div/div/input'
emailInput = '/html/body/div[1]/div/div[8]/div[1]/div/form/div[3]/div/div/input'
messageInput = '/html/body/div[1]/div/div[8]/div[1]/div/form/div[4]/textarea[1]'
submitEmail = '/html/body/div[1]/div/div[8]/div[1]/div/form/div[5]/button'

def sleep():
    time.sleep(5)

def initialize_browser():
    browser = webdriver.Chrome()
    browser.get("https://ivanveselinov.com")
    return browser

def scroll_to_about_us_section():
    # This will scroll to About Us section 
    browser = initialize_browser()
    about_us = browser.find_element("xpath", aboutUs)
    about_us.click()
    sleep()
    browser.quit()

def current_work_place():
    # This open current work space webpage
    browser = initialize_browser()
    dektech = browser.find_element("xpath", dek_tech)
    dektech.click()  
    sleep()
    browser.quit()


def previous_work_place():
    # This open current previous work space webpage
    browser = initialize_browser()
    ta = browser.find_element("xpath", team_assurance)
    ta.click()
    sleep()
    browser.quit()

def project5():
    # This will open Project 5
    browser = initialize_browser()
    ice_concrete = browser.find_element("xpath", iceConcrete)
    ice_concrete.click()
    sleep()
    browser.quit()

def project4():
    # This will open Project 4
    browser = initialize_browser()
    share_a_memory = browser.find_element("xpath", shareMemory)
    share_a_memory.click()
    sleep()
    browser.quit()

def project3():
    # This will open Project 3
    browser = initialize_browser()
    mls_system = browser.find_element("xpath", mls)
    mls_system.click()
    sleep()
    browser.quit()

def project2():
    # This will open Project 2
    browser = initialize_browser()
    uniquee_system = browser.find_element("xpath", uniquee)
    uniquee_system.click()
    sleep()
    browser.quit()

def project1():
    # This will open Project 1
    browser = initialize_browser()
    western_system = browser.find_element("xpath", westernSuburb)
    western_system.click()
    sleep()
    browser.quit()

def project0():
    # This will open Project 0
    browser = initialize_browser()
    tic_tac_toe = browser.find_element("xpath", ticTacToe)
    tic_tac_toe.click()
    sleep()
    browser.quit()

def techical():
    # This will scroll to Techinal Scills Section
    browser = initialize_browser()
    technical_skills = browser.find_element("xpath", technicalSkills)
    technical_skills.click()
    sleep()
    browser.quit()

def techical_skills_icons():
    # This will scroll to Techinal Skills Section Icons
    browser = initialize_browser()
    technical_skills_icon = browser.find_element("xpath", techicalSkillsIcons)
    technical_skills_icon.click()
    sleep()
    browser.quit()

def education():
    # This will scroll to Education Section
    browser = initialize_browser()
    education_section = browser.find_element("xpath", educationSection)
    education_section.click()
    sleep()
    browser.quit()

def publication():
    # This will scroll to Publication Section
    browser = initialize_browser()
    publication_section = browser.find_element("xpath", publicationSection)
    publication_section.click()
    sleep()
    browser.quit()

def send_email():
    # This will scroll to Publication Section
    browser = initialize_browser()
    name_input = browser.find_element("xpath", emailNameInput)
    name_input.send_keys('Ivan Veselinov')
    sleep()
    email_input = browser.find_element("xpath", emailInput)
    email_input.send_keys('ivan_veselinov@yahoo.com')
    sleep()
    message_input = browser.find_element("xpath", messageInput)
    message_input.send_keys('This message has been send from TA Automation!!')
    sleep() 
    send_message = browser.find_element("xpath", submitEmail)
    send_message.click()
    sleep()
    browser.quit()




scroll_to_about_us_section()
current_work_place()
previous_work_place()
project5()
project4()
project3()
project2()
project1()
project0()
techical()
techical_skills_icons()
education()
publication()
send_email()
    
    
