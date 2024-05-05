import time
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
driver = webdriver.Chrome(options=options)

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome\\User Data\\Default')

with webdriver.Chrome() as browser:
    browser.get('https://mingkh.ru/moskva/moskva/1027700430889/')

#    tags_input = browser.find_elements(By.xpath, //dl/dd[9] )






# https://mingkh.ru/moskva/moskva/1027700430889/html/body/div[1]/div[2]/div[2]/div[3]/div[1]/dl/dd[9]