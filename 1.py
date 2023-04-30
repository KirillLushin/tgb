    class User:
        def __init__(self, user_id, name, age, email):
            self.user_id = user_id
            self.name = name
            self.age = age
            self.email = email


    def get_user_info(user: User) -> str:
        return f'Возраст пользователя {user.name} - {user.age}, ' \
               f'а email - {user.email}'


    user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
    print(get_user_info(user_1))

    import requests
    import time

    # api_url = 'http://api.open-notify.org/iss-now.json'
    # response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response
    # if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    #    print(response.text)
    # else:
    #    print(response.status_code)    # При другом коде ответа выводим этот код
    API_URL: str = 'https://api.telegram.org/bot'
    API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
    BOT_TOKEN: str = '1214625504:AAEC5qSw0dJiW9AU3VJLjlCptje22x9TGTA'
    ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
    # TEXT: str = 'Ура! Классный апдейт!'
    # MAX_COUNTER: int = 100

    offset: int = -2
    counter: int = 0
    cat_response: requests.Response
    # chat_id: int

    # while counter < MAX_COUNTER:

    #    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    #   updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    #    if updates['result']:
    #        for result in updates['result']:
    #            offset = result['update_id']
    #            chat_id = result['message']['from']['id']
    #            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    #    time.sleep(1)
    #    counter += 1

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