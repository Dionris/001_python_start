# Генераторы Списка часть 1

# Структура
# [выражение for val in коллекция]

a = [0 for i in range(7)]
print(a)

b = [i for i in range(10)]
print(b)

c = [i ** 2 for i in range(10)]  # числа в квадрате
print(c)

d = [i % 4 for i in range(1, 15)]  # все числа деленные на 4
print(d)

c = [i * 5 for i in 'hello']
print(c)

e = [ord(i) for i in 'abcd']  # можем вписывать функции
print(e)

import random

f = [random.randint(-10, 10) for i in range(10)]
print(f)
f = [elem + 1 for elem in f]  # изменяем список 'f' тем что увеличиваем числа в нем на 1
g = [abs(elem) for elem in f]
print(g)

# Структура
# [выражение for val in коллекция if условие]

h = [abs(elem) for elem in f if elem % 2 == 0]  # можем добавить условия так что элементы могли делиться на 2
print(h)

k = [abs(elem) for elem in f if elem % 2 == 0 and elem % 3 == 0]  # можем добавить еще условия
print(h)

# Пример:
print('\nПример')

# нужно введенные данные преоброзовать из строк в целые числа
l = input().split()  # преобразуем в список разбивая каждое значение
l = [int(i) for i in l]  # осуществляем преоброзование с помощью генератора
print(l)


# Пример:
print('\nПример')
# проинициализируем двухмерный списко каким нибудь значением

n = 3
m = 6
p = [[0] * m for i in range(n)]  # создадим матрицу
print(p)  # можно убрать
p[1][3] = 100  # ИНИЦИАЛИЗИРУЕМ и проверяем если мы затроним один элемент, не затронит ли он остальные, ПОЛУЧИЛОСЬ!!!
for i in p:  # разложим полученную матрицу в столбик с помощью for
    print(i)


# Пример:
print('\nПример')
# в генераторах списка можно использовать двойные циклы

r = [(i,j) for i in 'abc' for j in [1,2,3]]
print(r)

# или усложним условия

r = [i*j for i in [2,3,4,5] for j in [1,2,3] if i*j>10]
print(r)
