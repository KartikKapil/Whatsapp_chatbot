from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from requests import get
from bs4 import BeautifulSoup as bs
import keyboard
import time
import click
import os
import sys
import csv
import threading
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

import nlp_stage2

driver = webdriver.Chrome("/home/kartik/Downloads/chromedriver_linux64 (4)/chromedriver")



driver.get('https://web.whatsapp.com/')

input("press enter to continue")
contact = "Manav Bhai"
searchbox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchbox.send_keys(contact)
driver.implicitly_wait(20)
name = driver.find_element_by_class_name("_3dtfX")
elem = name
ac = ActionChains(driver)
ac.move_to_element(elem).click().perform()
time.sleep(2)

url = driver.page_source

def repeatfun():
    # threading.Timer(5.0,repeatfun).start()
    url = driver.page_source
    soup = bs(url,"lxml")
    try:
        gotdiv = soup.find_all("div",class_="msd msg-group")
    except IndexError:
        gotdiv = 'null'

    div = soup.find_all("div",class_="copyable-text")[-2]
    for date in soup.find_all("div",class_="copyable-text"):
        if len(list(date))!=0:
            
            kam=date.get("data-pre-plain-text") 

    kam=list(kam)
    ind=kam.index("]")
    name_user=""
    for i in range(ind+2,len(kam)-2):
        name_user+=str(kam[i])


    text = div.find_all("span")
    try:
        gottext = text[1].find_all(text=True)
        message = str(gottext[0].string)
    except IndexError:
        gottext = 'null'

    

    print(name_user, message)
    if name_user == "Kartik Kapil":
        print("you repled last no need to chat")
    else:
        with open('dict.csv', "r") as f:
            reader = csv.reader(f)
            chat={}
            for row in reader:
                key = row[0]
                chat[key] = row[1:]

        try:
            # gotreply= chat[message]
            gotreply= nlp_stage2.final_fuction(message)
            print(gotreply)
        except KeyError:
            gotreply= "null"
            print("no reply")

    
        if gotreply == 'null':
            string = "Sorry! I didn't understand. I'm still learning."
            messagebox= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            messagebox.send_keys(string)
            messagebox.send_keys(Keys.RETURN)
        else:
            messagebox= driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            messagebox.send_keys(gotreply)
            messagebox.send_keys(Keys.RETURN)

repeatfun()