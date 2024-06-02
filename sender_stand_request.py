#Импорты всех файлов + requests
import requests
import configuration
import data
import create_kit_name_kit_test

#Создание пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#Сохранение нового пользователя в переменную
response = post_new_user(data.user_body)

#Присвоение токена переменной без лишних символов
authToken = response.json()["authToken"]

#Всякие проверки
print(response.status_code)
print(response.json())
print(authToken)




