from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome("/home/kartik/Downloads/chromedriver_linux64 (4)/chromedriver")
# driver =webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

input("press enter to start")

#chechsign = driver.find_element_by_class_name("ZKn2B")
#chechsign = driver.find_element_by_class_name("_31gEB")
#chechsign.click()
try:
    chechsign = driver.find_element_by_class_name("_31gEB")
    print("elemrnt found")
    contact = driver.find_element_by_class_name("_3ko75 _5h6Y_ _3Whw5")
    print(contact.getText())
except NoSuchElementException:
    print("no such element found")