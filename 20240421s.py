from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url = 'https://happypython.ru/about_us/'
service = Service(executable_path='C:/chromedriver/chromedriver')  # указываем путь до драйвера
browser = webdriver.Chrome(service=service)
try:
    browser.get(url)
    time.sleep(10)
    browser.quit()
except Exception as ex:
    print(ex)
    browser.quit()
browser.quit()