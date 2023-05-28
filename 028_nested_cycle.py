# Вложенный цикл

for i in range(3):
    for j in range(5):
        print(i, end='')  # убираем переносы
    print()  # перенос на новую строчку делается пустым принтом

print('')

for i in range(3):
    for j in range(5):
        print(j, end='')  # убираем переносы
    print()  # перенос на новую строчку делается пустым принтом

print('')

for i in range(3):
    for j in range(i):
        print(j, end='')  # убираем переносы
    print()  # перенос на новую строчку делается пустым принтом

print('')

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, end='')  # убираем переносы
    print()  # перенос на новую строчку делается пустым принтом

print('')

for i in range(1, 4):
    for j in range(10, 13):
        print(i, j)

print('')

for i in 'ab':
    for j in 'cdf':
        print(i, j)

# Пример
# длина пароля 3

from string import printable

print(printable)

# for b1 in printable:
#    for b2 in printable:
#        for b3 in printable:
#            print(b1,b2,b3)


# Еще пример
# перемножаем чисел, получим таблицу умножения

for i in range(1, 10):
    for j in range(1, 11):
        print(j, '*', i, '=', j * i, end='  ')
    print()

# Пример
# Сколько шестибуквенных слов, начинающихся и заканчивающихся
# согласной буквой и содержащих ровно 2 гласные, можно составить
# из букв Т, Ы, К, В, А? Каждая из допустимых букв
# может входить в словонесколько раз.

k=0

for b1 in 'tukva':
    for b2 in 'tukva':
        for b3 in 'tukva':
               for b4 in 'tukva':
                    for b5 in 'tukva':
                        for b6 in 'tukva':
                            rez = b1+b2+b3+b4+b5+b6
                            if rez[0] in 'tkv' and rez[-1] in 'tkv': # если первая буква будет из этих букв (tkv), и если последняя буква также из этих букв (tkv) то выводим результат
                                if rez.count('a')+rez.count('u')==2: # если 'a' или 'u' равно двум то это слово нам и нужно
                                    k+=1 # подсчитаем количество слов которых получилось
                                    print(rez) # выведем все слова получившие
print(k)


# Пример
# Узнать сумму всех чисел одного числа

# x=int(input())
# s=0
# while x>0:  # цикл работает пока есть числа у нашего числа
#     s+= x%10  # Прибавляем последнию цифру числа x к s
#     x//=10  # и паралельно убираем последнюю цифру числа x
#
# print(s)


# Можем совмещать два вида циклов

for i in range (1,100001):
    x=i
    s=0
    while x>0:  # цикл работает пока есть числа у нашего числа
        s+= x%10  # Прибавляем последнию цифру числа x к s
        x//=10  # и паралельно убираем последнюю цифру числа x
    print(i,s)