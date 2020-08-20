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


driver = webdriver.Chrome("/home/kartik/Downloads/chromedriver_linux64 (4)/chromedriver")



driver.get('https://web.whatsapp.com/')

input("press enter to continue")

# target = 'Ravi Jain Jiit'

# #panel = driver.find_element_by_class_name('chatlist-panel-body')

# elem = None
# a = 0
# while elem is None:
#     a += 300
#     try:
#         #driver.execute_script('arguments[0].scrollTop = %s' %a, panel)
#         print("reaching here")
#         elem = driver.find_element_by_xpath('//span[@title=' + target + ']')
#     except:
#             pass
contact = "Chachi"
searchbox = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
searchbox.send_keys(contact)
#driver.maximize_window()
driver.implicitly_wait(20)

#sendbutton = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[12]/div')
name = driver.find_element_by_class_name("_3dtfX")
# name.click()
elem = name
print("working")
ac = ActionChains(driver)
ac.move_to_element(elem).click().perform()
time.sleep(2)

url = driver.page_source

print("working till here")
def repeatfun():
    # threading.Timer(5.0,repeatfun).start()
    url = driver.page_source
    soup = bs(url,"lxml")
    print("fuction called")
    try:
        # gotdiv = soup.find_all("div",{"class":"msd msg-group"})
        gotdiv = soup.find_all("div",class_="msd msg-group")
    except IndexError:
        gotdiv = 'null'
    
    # if gotdiv == 'null':
    #     # div = soup.find_all("div",{"class":"bubble bubble-text copyable-text"})[-1]
    #     div = soup.find_all("div",class_="copyable-text")[-1]
    #     print(div)
    # else:
    #     div = soup.find_all("div",class_="copyable-text")[-1]
    #     print(div)
    #     # div = soup.find_all("div",{"class":"msg msg-group"})[-1]
    div = soup.find_all("div",class_="copyable-text")[-2]
    # print("div1-->")
    # print(div)
    for date in soup.find_all("div",class_="copyable-text"):
        # print("date--->")
        # print(len(list(date)))
        if len(list(date))!=0:
            
            kam=date.get("data-pre-plain-text") 
            
        # print(date.get("data-pre-plain-text"))
    print("kam-->")
    print(kam)
    kam=list(kam)
    ind=kam.index("]")
    name_user=""
    for i in range(ind+2,len(kam)-2):
        name_user+=str(kam[i])

    print(name_user)

    text = div.find_all("span")
    # print("text1--->")
    # print(text[1])
    # print("text(all)--->")
    # print(text)
    try:
        gottext = text[1].find_all(text=True)
        print("gottext--->")
        print(gottext[0].string)
        # gottext = text[4].find_all(text=True)[1]
    except IndexError:
        gottext = 'null'

    if gottext == 'null':
        # div = soup.find_all("div", { "class" : "chat-title" })[-1]
        div = soup.find_all("div", class_="chat-title")
        print(div)
        name = div.find_all(text=True)[1]
        try:
            msg = text[-2].find_all(text=True)[1].lower()
        except IndexError:
            msg = "You replied last"
        time = text[-1].find(text=True)

    else: #group
        div2=soup.find_all("div",class_="_2hqOq message-in focusable-list-item")
        print("div2---->")
        print(div2)
        name=div2[0].find_all(class_="_18lLQ")
        # name = name[0]['value']
        print("name--->")
        print(name)
        # name = text[0].find_all(text=True)
        # name = text[3].find_all(text=True)[1]
        try:
            msg = text[1].find_all(text=True)[1].lower()
        except IndexError:
            msg = "You replied last"
        try:
            time = text[-2].find(text=True)
        except:
            time = "None"


    print(name, msg, time)
    print("congo you reached somewhere kamal ho gaya")
    try:
        prevmsg = prevmsg
    except:
        prevmsg = "first"

    try:
        prevtime = prevtime
    except:
        prevtime = "first"
    if "buddy" in msg:

        with open('dict.csv', "r") as f:
            reader = csv.reader(f)
            chat = {}

            for row in reader:
                key = row[0]
                chat[key] = row[1:]
        try:
            gotreply = chat[msg]
        except KeyError:
            gotreply = 'null'

        print(gotreply)

    if gotreply == 'null':
        string = "Sorry! I didn't understand. I'm still learning."
        input_box = driver.find_element_by_class_name('pluggable-input-body')
        input_box.send_keys(string)
        driver.find_element_by_xpath('//span[@data-icon="send"]').click()
    else:
        input_box = driver.find_element_by_class_name('pluggable-input-body')
        input_box.send_keys(gotreply)
        driver.find_element_by_xpath('//span[@data-icon="send"]').click()

repeatfun()