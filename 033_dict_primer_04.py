# 4 - Храниние данных об обьекте

contacts = {
    "John Kennedy":{
        'birthday': "29 may 1917", 'city': 'Brookline',
        'phone': None, 'children': 3
    },
    "Arnold Schwarzenegger":{
        'birthday': "30 july 1947", 'city':'Gradec',
        'phone': '555-555-555', 'children': 5
    },
    "Donald John Trump":{
        'birthday': "14 july 1946", 'city': 'New York',
        'phone': '777-777-777', 'children': 4
    }
}

persons = (contacts.keys())
#print(persons)
for person in persons: #достаем всю информацию о человеке (ПРИМЕР 1)
    birthday = contacts[person]['birthday']
    city = contacts[person]['city']
    phone = contacts[person]['phone']
    children = contacts[person]['children']
    print(person,birthday,city,children,phone)

for person in persons: #достаем всю информацию о человеке (ПРИМЕР 2)
    print(person)
    for data in contacts[person]:
        print(data, contacts[person][data])
