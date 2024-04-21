from LxmlSoup import LxmlSoup
import requests

st_accept = "text/html" # говорим веб-серверу,
                        # что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

html = requests.get('https://sunlight.net/catalog').text  # получаем html код сайта
soup = LxmlSoup(html)  # создаём экземпляр класса LxmlSoup

links = soup.find_all('a', class_='cl-item-link js-cl-item-link js-cl-item-root-link')  # получаем список ссылок и наименований
for i, link in enumerate(links):
    url = link.get("href")  # получаем ссылку товара
    name = link.text()  # извлекаем наименование из блока со ссылкой
    price = soup.find_all("div", class_="cl-item-info-price-discount")[i].text()  # извлекаем цену
    print(i)
    print(f"Url - {url}")
    print(f"Name - {name}")
    print(f"Price - {price}\n")