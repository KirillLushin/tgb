from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://parsinger.ru/selenium/1/1.html")

# Получение списка полей
fields = driver.find_elements(By.XPATH,"//input[@type='text']")

# Ввод текста в каждое поле
for field in fields:
 field.send_keys("Ваш текст")
 field.send_keys(Keys.TAB) # Перемещение к следующему полю

button = driver.find_element(By.ID,"btn")
button.click()

# Используйте явное ожидание, чтобы дождаться загрузки страницы
time.sleep(1)
result = driver.find_element(By.ID,"result")
print(result.text)


time.sleep(5)

driver.quit()