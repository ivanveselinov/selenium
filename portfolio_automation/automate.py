from selenium import webdriver
import xpath # Import xpath.py
import time

def sleep():
    time.sleep(5)

def initialize_browser():
    browser = webdriver.Chrome()
    browser.get("https://ivanveselinov.com")
    return browser

def scroll_to_about_us_section():
    # This will scroll to About Us section 
    browser = initialize_browser()
    about_us = browser.find_element("xpath", xpath.aboutUs)
    about_us.click()
    sleep()
    browser.quit()

def current_work_place():
    # This open current work space webpage
    browser = initialize_browser()
    dektech = browser.find_element("xpath", xpath.dek_tech)
    dektech.click()  
    sleep()
    browser.quit()


def previous_work_place():
    # This open current previous work space webpage
    browser = initialize_browser()
    ta = browser.find_element("xpath", xpath.team_assurance)
    ta.click()
    sleep()
    browser.quit()

def project5():
    # This will open Project 5
    browser = initialize_browser()
    ice_concrete = browser.find_element("xpath", xpath.iceConcrete)
    ice_concrete.click()
    sleep()
    browser.quit()

def project4():
    # This will open Project 4
    browser = initialize_browser()
    share_a_memory = browser.find_element("xpath", xpath.shareMemory)
    share_a_memory.click()
    sleep()
    browser.quit()

def project3():
    # This will open Project 3
    browser = initialize_browser()
    mls_system = browser.find_element("xpath", xpath.mls)
    mls_system.click()
    sleep()
    browser.quit()

def project2():
    # This will open Project 2
    browser = initialize_browser()
    uniquee_system = browser.find_element("xpath", xpath.uniquee)
    uniquee_system.click()
    sleep()
    browser.quit()

def project1():
    # This will open Project 1
    browser = initialize_browser()
    western_system = browser.find_element("xpath", xpath.westernSuburb)
    western_system.click()
    sleep()
    browser.quit()

def project0():
    # This will open Project 0
    browser = initialize_browser()
    tic_tac_toe = browser.find_element("xpath", xpath.ticTacToe)
    tic_tac_toe.click()
    sleep()
    browser.quit()

def techical():
    # This will scroll to Techinal Scills Section
    browser = initialize_browser()
    technical_skills = browser.find_element("xpath", xpath.technicalSkills)
    technical_skills.click()
    sleep()
    browser.quit()

def techical_skills_icons():
    # This will scroll to Techinal Skills Section Icons
    browser = initialize_browser()
    technical_skills_icon = browser.find_element("xpath", xpath.techicalSkillsIcons)
    technical_skills_icon.click()
    sleep()
    browser.quit()

def education():
    # This will scroll to Education Section
    browser = initialize_browser()
    education_section = browser.find_element("xpath", xpath.educationSection)
    education_section.click()
    sleep()
    browser.quit()

def publication():
    # This will scroll to Publication Section
    browser = initialize_browser()
    publication_section = browser.find_element("xpath", xpath.publicationSection)
    publication_section.click()
    sleep()
    browser.quit()

def send_email():
    # This will scroll to Publication Section
    browser = initialize_browser()
    name_input = browser.find_element("xpath", xpath.emailNameInput)
    name_input.send_keys('Ivan Veselinov')
    sleep()
    email_input = browser.find_element("xpath", xpath.emailInput)
    email_input.send_keys('ivan_veselinov@yahoo.com')
    sleep()
    message_input = browser.find_element("xpath", xpath.messageInput)
    message_input.send_keys('This message has been send from TA Automation!!')
    sleep() 
    send_message = browser.find_element("xpath", xpath.submitEmail)
    send_message.click()
    sleep()
    browser.quit()

