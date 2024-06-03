#Импорт файла sender_stand_request
#import sender_stand_request

#Заголовок для создания пользователя
headers = {
    "Content-Type": "application/json"
}

#Тело для создания пользователя
user_body = {
    "firstName": "Анатолий",  # Имя пользователя
    "phone": "+79995553322",  # Контактный телефон пользователя
    "address": "г. Москва, ул. Пушкина, д. 10"  # Адрес пользователя
}

#Заголовок для запроса на создание набора пользователя
#headers_for_kit = {
#    "Content-Type": "application/json",
#    "Authorization": sender_stand_request.authToken
#}

