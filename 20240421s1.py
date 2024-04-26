import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService

with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as driver:
    driver.get("https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/%D0%B5%D0%B4%D0%B8%D0%BD%D1%8B%D0%B9-%D1%80%D0%B5%D0%B5%D1%81%D1%82%D1%80-%D0%B7%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%89%D0%B8%D0%BA%D0%BE%D0%B2/%D0%B7%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%89%D0%B8%D0%BA/3980")
    time.sleep(15)