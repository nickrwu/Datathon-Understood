from selenium import webdriver
import requests
import pandas as pd

guideData = pd.read_csv("stitchedGuide.csv")

guideLink = guideData[guideData["Link to GS Profile"]]

browser = webdriver.Chrome('/usr/local/bin/chromedriver')

def copyMission(url):
    url = guideData[i]

    #Open login page
    browser.get('url')

    #Enter login info:
    elementID = browser.find_element_by_name('j_username')
    elementID.send_keys('***REMOVED***')

    elementID = browser.find_element_by_name('j_password')
    elementID.send_keys('***REMOVED***')
    #Note: replace the keys "username" and "password" with your LinkedIn login info
    elementID.submit()

#Go to webpage

