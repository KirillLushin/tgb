# https://stepik.org/lesson/731861/step/5?unit=733396
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://parsinger.ru/selenium/2/2.html")

# Получение списка полей
fields = driver.find_elements(By.PARTIAL_LINK_TEXT,"16243162441624")

# Ввод текста в каждое поле
for field in fields:
 field.click()

field2 = driver.find_elements(By.ID,'result')
print(field2)

time.sleep(5)

driver.quit()