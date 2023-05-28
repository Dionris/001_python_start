# Пример
d = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four"
}
print(d)
print(len(d))
if 4 in d:
    print(d[4])
else:
    d[4] = 'five'
print(d)

print(d)
for key in d:
    print(key, d[key])


# Методы словаря:
print('\n Методы словаря:')

# Получаем значение ключа
print('\n Получаем значение ключа \n')

print(d.get(1))

print(d.get(5, 'Значение по умолчанию'))

print(d.get(3, 'Значение по умолчанию'))


# Получаем значение ключа либо создает новую пару если ее нет
print('\n Получаем значение ключа либо создает новую пару если ее нет \n')

print(d.setdefault(2, "Присваиваем значение которого нет"))

d.setdefault(7, "Присваиваем значение которого нет")
print(d)


# возвращает значение и удоляет его из словаря
print('\n возвращает значение и удоляет его из словаря \n')

print(d.pop(3))
print(d)


# удаляет последнее значение из словаря
print('\n удаляет последнее значение из словаря \n')

print(d.popitem())
print(d.popitem())
print(d)


# возвращает ключи всех значений словаря
print('\n возвращает ключи всех значений словаря \n')

print(d.keys())

print(d.keys())
for key in d.keys():
    print(key, d[key])


# Возвращаем все значения словаря без ключей
print('\n Возвращаем все значения словаря без ключей \n')

print(d.values())

d.values()
for value in d.values():
    print(value)


# возращает коллекцию где содержаться все пары
print('\n возращает коллекцию где содержаться все пары \n')

print(d.items())
for para in d.items():
    print(para)
for para in d.items():
    print(para[0], para[1])
for para in d.items():
    print(para[0])

for key,value in d.items():
    print(key,value)


# Очищаем словарь
print('\n Очищаем словарь \n')

d.clear()
print(d)
