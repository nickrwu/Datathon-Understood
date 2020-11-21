from selenium import webdriver
import requests
import pandas as pd
import random
import time

guideData = pd.read_csv("../Data/stitchedGuide.csv")
# Importing the links from csv
guideLink = guideData["Link to GS Profile Page"]

browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

agents = open("Chrome.txt", "r")
content = agents.read()
user_agent_list = content.splitlines()
#  user_agent_list = [line for line in agents.splitlines().readlines()]
agents.close()
# print(user_agent_list)


# Defining the copy function
def copyMission(url):
    # Rotating through User Agents
    head = 'https://httpbin.org/headers'
    # for i in range(1, len(user_agent_list)):
    #Pick a random user agent
    user_agent = random.choice(user_agent_list)
    #Set the headers 
    headers = {'User-Agent': user_agent}
    #Make the request
    response = requests.get(head,headers=headers)
     
    print("Request #%d\nUser-Agent Sent:%s\n\nHeaders Recevied by HTTPBin:"%(i,user_agent))
    print(response.json())
    print("-------------------")

    #Open Page
    browser.get(url)
    
    time.sleep(2)
    
    #Save Mission Statement:
    mission = browser.find_element_by_id('mission-statement').text
    guideData["mission"] = mission
    
    

for i in range(len(guideLink)):
    dataURL = guideLink[i]
    copyMission(dataURL)
print(guideData)

