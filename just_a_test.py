from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/home/kartik/Downloads/chromedriver_linux64 (4)/chromedriver")

driver.get("https://techwithtim.net/")

print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)


#driver.quit()