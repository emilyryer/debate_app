import time
from selenium import webdriver
import test_functions

driver = webdriver.Chrome('chromedriver.exe')  # chromedriver.exe is included in the selenium_tests/chrome folder
driver.get('http://127.0.0.1:8000/');
time.sleep(2) # Let the user actually see something!

email = test_functions.generateTestEmail()
test_functions.register(email, 'create_test', 'create_pass', driver)

test_functions.createRoom('Test', 'Test Question')

driver.quit() #terminates program
