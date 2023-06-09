import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '1214625504:AAEC5qSw0dJiW9AU3VJLjlCptje22x9TGTA'
offset: int = -2
timeout: int = 1
updates: dict

API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
# TEXT: str = 'Ура! Классный апдейт!'
# MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
cat_response: requests.Response


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1