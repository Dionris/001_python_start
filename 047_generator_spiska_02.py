# Генераторы списков часть 2

a = [
    ('Sidorov', 1995),
    ('Lukov', 2002),
    ('Petrov', 1991),
    ('Gorbachev', 1984),
    ('Kostin', 2000),
    ('Isaev', 2005),
    ('Eliseev', 1999),
    ('Kozlov', 2004),
    ('Bukov', 1995),
    ('Gavrilov', 1980),
    ('Efrimov', 2006),
]

print(a[4][0])  # обращаемся к 5 человеку

# теперь при помощи генератора списка будем достовать интересующие нам значения
b = [elem[0] for elem in a]  # только именя
print(b)

b = [elem[1] for elem in a]  # только даты
print(b)

b = [elem[0] for elem in a if elem[0].startswith('E')]  # выписываем людей с фамилией на букву 'E'
print(b)

b = [elem[0] for elem in a if elem[1] > 2000]  # выписываем людей с фамилией родившимися после 2000 года
print(b)

b = [elem[0][0] for elem in a if elem[1] > 2000]  # выписываем первую букву людей с фамилией родившимися после 2000 года
print(b)

# Пример 2
print('\nПример 2')

# у нас есть вложенный словарь
c = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'BMW'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
    'Gavrilov': {'age': 1980, 'hobby': 'tennis', 'car': 'Audi'},
    'Efrimov': {'age': 2006, 'hobby': 'music', 'car': 'Opel'},
}

d = [elem for elem in c]
print(d)  # видим что ключи у них фамилии

d = [c[elem]['car'] for elem in c]  # теперь обращаемся по ключу машина
print(d)

d = [(elem, c[elem]['car']) for elem in c if c[elem]['age'] < 2000 and c[elem]['hobby'] == 'soccer']
# теперь выведим фамилии и машины тех кто младше 2000 года и люби футбол
print(d)

# Пример 3
print('\nПример 3')
# из строки выберем только цифры

s = 'jdkfn1ldsnlkvs3vnlksdnv3avjlnw7adsgvjs'

bb = [int(i) for i in s if i.isdigit()]  # метод isgigit - вызывает только цифры
print(bb)

bb = [i for i in s if i.isalpha()]  # метод isalpha - вызывает только буквы
print(bb)

# Пример 4
print('\nПример 4')

import random

n = 7
m = 7

aa = [[random.randint(1, 6) for j in range(m)] for i in range(n)]  # Написали вложенный генератор который заполнил
# двухмерный список (похож с работой вложенных циклов)
for i in aa:
    print(i)

bbb = [aa[i][j] for i in range(n) for j in range(m) if i == j]  # будем брать числа с главной диагонали
print('Главная диагональ', bbb)
ccc = [aa[2][j] for j in range(m)]  # будем обращаться к третьей строке
print('3 строка', ccc)
dd = [aa[i][-1] for i in range(n)]  # будем обращаться к последнему столбцу
print('последний столбец', dd)

# Пример 5
print('\nПример 5')

# составим таблицу умножения
nn = 10
mm = 10

aaa = [[i * j for j in range(1, mm+1)] for i in range(1, nn+1)]
for i in aaa:
    print(i)
