#Задача Кодекс Охотников за цифрами: https://stepik.org/lesson/731861/step/6?unit=733396

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://parsinger.ru/selenium/3/3.html")
common_blocks = driver.find_elements(By.TAG_NAME, "p")
total = 0
for block in common_blocks:
 total += int(block.text)
print("Сумма:", total)
