import os
import requests
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def initiateSelenium():
    # create a new Chrome session
    driver = webdriver.Chrome("C:\\Users\\anshu\\PycharmProjects\\instaCrawler\\chromedriver.exe")
    driver.implicitly_wait(30)
    driver.maximize_window()
    return driver


def instaProfileCrawler():
    driver = initiateSelenium()
    # Navigate to the application home page
    driver.get("https://www.instagram.com/mrunu/")
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    instaProfile = driver.find_element_by_class_name("_7UhW9")
    profilePic = driver.find_element_by_class_name("_6q-tv")
    profileName = soup.find('h1',{'class':'rhpdm'})
    profileInfo = soup.findAll('a',{'class': '-nal3'})


    print("Name: " + profileName.text)
    print("Username: " + instaProfile.get_attribute("innerHTML"))
    print("Profile pic link: " + str(profilePic.get_attribute("src")))
    print("Number of posts: " + profileInfo[0].text)
    print("Follwers: " + profileInfo[1].text)
    print("Following: " + profileInfo[2].text)
    soup = BeautifulSoup(driver.page_source, 'html.parser')


    Pagelength = driver.execute_script("window.scrollTo(0,document.body.scrollHeight)/1.5;")
    links = []
    source = driver.page_source
    data = BeautifulSoup(source,'html.parser')
    body = data.find('body')
    script = body.find('span')
    for link in script.findAll('a'):
        if re.match("/p", link.get('href')):
            links.append('https://www.instagram.com'+link.get('href'))
    # sleep time is required. If you don't use this Instagram may interrupt the script and doesn't scroll through pages
    time.sleep(5)
    Pagelength = driver.execute_script("window.scrollTo(document.body.scrollHeight/1.5, document.body.scrollHeight/3.0);")
    source = driver.page_source
    data= BeautifulSoup(source, 'html.parser')
    body = data.find('body')
    script = body.find('span')
    for link in script.findAll('a'):
        if re.match("/p", link.get('href')):
            links.append('https://www.instagram.com'+link.get('href'))
    print("Post collected:")
    print(len(links))
    for link in links:
        print("src:" + link)
        print("="*200)



    """"
    listOfImages = soup.findAll('img',{'class': 'FFVAD'})
    print(len(listOfImages))
    for item in listOfImages:
        src = item.get('src')
        print("src: " + src)
        print("="*200)

    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        listOfImages = soup.findAll('img',{'class': 'FFVAD'})
        print(len(listOfImages))
        if(len(listOfImages) < int(soup.find('span',{'class':'g47SY'}).text)):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            break
"""




instaProfileCrawler()




