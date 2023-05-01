import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '1214625504:AAEC5qSw0dJiW9AU3VJLjlCptje22x9TGTA'
offset: int = -2
timeout: int = 1
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    time.sleep(3)
    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')