from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
driver = webdriver.Chrome("/home/kartik/Downloads/chromedriver_linux64 (4)/chromedriver")
# driver =webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

input("press enter to start")

contact = "Work"
text = "hello from me "

searchbox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchbox.send_keys(contact)
#driver.maximize_window()
driver.implicitly_wait(20)

#sendbutton = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[12]/div')
sendbutton = driver.find_element_by_class_name("_3dtfX")
sendbutton.click()
messagebox= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
messagebox.send_keys(text)
messagebox.send_keys(Keys.RETURN)

# sendbutton2= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
# sendbutton2.click()