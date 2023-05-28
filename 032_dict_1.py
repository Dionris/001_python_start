# СЛОВАРЬ

ab = {          # key : value
         'Swaroop'    : 'swaroop@swaroopch.com',
         'Larry'      : 'larry@wall.org',
         'Matsumoto'  : 'matz@ruby-lang.org',
         'Spammer'    : 'spammer@hotmail.com'
     }

# Обращения к переменной в словаре по ключу - ab['Swaroop']
print("Адрес Swaroop'а:", ab['Swaroop'], "\n")

# Функция запроса полного списка
def spisok():
    for name, address in ab.items():
        print('Контакт {0} с адресом {1}'.format(name, address))

spisok()

# Удаление пары ключ-значение
del ab['Spammer']

print('\nВ адресной книге {0} контакта\n'.format(len(ab)))

spisok()

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'], "\n")

spisok()



# Новый пример
# Создаем пустой словарь
person = {}
s = "Morunov Vladislav Minsk BNTU 9 8 6 8 7"
s = s.split()
person['lastName'] = s[0]
person['firstName'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(s)
print(person)