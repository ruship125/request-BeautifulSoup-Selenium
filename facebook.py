import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver\chromedriver.exe') # Path of Chrome Driver
browser.get('https://www.facebook.com/login')
emailElem = browser.find_element_by_id('email')
emailElem.send_keys('xyz@xyz.com') # Your Email Goes HEre
passwordElem = browser.find_element_by_id('pass')
passwordElem.send_keys('xyz') # Your Password Goes Here
passwordElem.submit()
time.sleep(900) # Time limit Goes Here Now Its Set to 900 seconds that is 15 Min.
browser.quit()
