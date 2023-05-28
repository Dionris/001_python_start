#  JSON - JavaScript Nation Object

# load считываем файл в формате json
# loads  считываем строку в формате json
#
# Методы:
# dump - создает файл json
# dumps - создает строку в виде json

import json
from random import randint
from datetime import datetime

str_json = """
{
    "response": {
        "count": 5961878,
        "items": [{
            "first_name": "Елизавета",
            "id": 620471795,
            "last_name": "Сопова",
            "can_access_closed": true
        }, {
            "first_name": "Роман",
            "id": 614752515,
            "last_name": "Малышев",
            "can_access_closed": true
        }]
    }
}
"""
# Распаршиваем JSON файл
print(type(str_json))

data = json.loads(str_json)
print(type(data))
print(data)
print(data['response']['count'])  # обращаемся по ключу получить значения
print(type(data['response']['items']))
print(data['response']['items'])

for item in data['response']['items']:  # перебираем значения в ключе словаря 'response' а в нем в словаре 'items'
    print(type(item))
    print(item)
    print(item['first_name'], item['last_name'])  # распаршиваем данные только с именем и фамилией

# изменяем JSON файл
for item in data['response']['items']:
    del item['id']  # удаляем ключ
    item['likes'] = randint(100, 200)  # добовляем ключ likes
    item['a'] = None
    item['now'] = datetime.now().strftime('%d.%m.%y')  # strftime('%d.%m.%y') - переводит datetime в строку

print(data['response']['items'])  # проверяем

# создаем свой JSON
new_json = json.dumps(data, indent=2)  # indent - создает отступы в json файле
print(new_json)  # русские слова преобразуются в unicode слова

print(json.loads(new_json))  # преобразуем json вновь в словарь и видим что русские слова отображаются нормально

# Сохраняем наш Json в отдельный файл
with open('073_my.json', 'w') as file:  # 'w' - открываем на запись
    json.dump(data, file, indent=3)  # записываем data в json и делаем отступы в 3 пробела чтобы лекче прочитать

# Открываем на чтение JSON
with open('073_my.json', 'r') as file:  # 'r' - читаем на запись
    data = json.load(file)  # забираем из file и записываем в data

print(data)
print(type(data))
