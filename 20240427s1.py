import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    # Получение списка полей
    # fields = browser.find_elements((By.CLASS_NAME, 'form')

    # Ввод текста в каждое поле
    for field in fields:
        input_form = browser.find_element(By.CLASS_NAME, 'form').send_keys('Text')
        field.send_keys(Keys.TAB)  # Перемещение к следующему полю


time.sleep(5)
