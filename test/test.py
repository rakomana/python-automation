from selenium import webdriver
import requests
from selenium.webdriver.common.by import By

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://smartmortgagesuk.com/')

links = driver.find_elements(By.TAG_NAME, "a")
images = driver.find_elements(By.TAG_NAME, "img")

for link in links:
    r = requests.head(link.get_attribute('href'))
    print(link.get_attribute('href'), r.status_code)

# a robot bot to request 1000000 quotes


print("Total number of links on the site:", len(links))
print("Total number of images on the site:", len(images))