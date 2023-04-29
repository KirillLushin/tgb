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


api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response

if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)    # При другом коде ответа выводим этот код

