from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd

browser = webdriver.Chrome('/usr/local/bin/chromedriver')

#Open login page
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#Enter login info:
elementID = browser.find_element_by_id('username')
elementID.send_keys('InputUsername')

elementID = browser.find_element_by_id('password')
elementID.send_keys('InputPassword')
#Note: replace the keys "username" and "password" with your LinkedIn login info
elementID.submit()

#Go to webpage
browser.get('https://www.linkedin.com/company/google/')

request = requests.get('https://api.scrapingdog.com/linkedin/?api_key=5eaa61a6e562fc52fe763tr516e4653&type=company&linkId=google/about/').text

soup = BeautifulSoup(request,'html.parser')
l = {}
u = list()

# Company Name
try:
    l["Company"] = soup.find("h1",{"class":"org-top-card-summary__title t-24 t-black  truncate"}).text.replace("\n","")
except:
    l["Company"] = None
 
allProp = soup.find_all("dd",{"class":"org-page-details__definition-text t-14 t-black--light t-normal"})

# Properties from the Prop List
try:
    l["website"]=allProp[0].text.replace("\n","")
except:
    l["website"]=None
try:
    l["Industry"]=allProp[1].text.replace("\n","")
except:
    l["Industry"]=None
try:
    l["Company Size"]=soup.find("dd",{"class":"org-about-company-module__company-size-definition-text t-14 t-black--light mb1 fl"}).text.replace("\n","")
except:
    l["Company Size"]=None
try:
    l["Address"]=allProp[2].text.replace("\n","")
except:
    l["Address"]=None
try:
    l["Type"]=allProp[3].text.replace("\n","")
except:
    l["Type"]=None
try:
    l["Specialties"]=allProp[4].text.replace("\n","")
except:
    l["Specialties"]=None


u.append(l)
df = pd.io.json.json_normalize(u)

df.to_csv('linkedin.csv', index=False, encoding='utf-8')
print(df)