# Метод подсчета, Сортировка подсчетов

# Пример
# подсчитываем сколько повторяющих цифр в нашем списке (0,1,2,3,4,5)
a = [0, 1, 2, 5, 2, 4, 5, 1, 2, 4, 5, 1, 2, 1, 4, 0]
count = [0] * 6
for i in a:
    count[i] += 1
print(count)

for i in range(6):  # перебираем все возможные числа списка
    if count[i] > 0:  # проверка, не выводим значения которые не встречались
        # print(i, count[i])  # выводим все возможные числа и кол-во их повторений
        print((str(i) + ' ') * count[i], end='')  # сортируем список по возростанию

# Пример
print('\n Пример')
# Нужно из списка 's' подсчитать кол-во всех повторяющих букв
s = 'abczKljfsd KFDJKL dfn kaldfKLFAKL 343 (*/+-#$#():'
letters = [0] * 26  # создаем пустой список для алфавита, зная что там 26 букв
for i in s.lower():  # lower - для создания маленьких букв
    if i >= 'a' and i <= 'z':  # i - выводит от маленькой буквы 'a' до 'z', т.е. отсикаем символы
        # print(i,ord(i))  # ord - получает индекс букв (они по возростанию от a-z), из него видем что у 'a' = 97
        nomer = ord(i) - 97  # и получается отнимает 'a' от 97 и получаем 0 - это будет первая буква в списке
        print(i, nomer)  # видим результат того что у каждой буквы свой индекс есть
        letters[nomer] += 1  # собираем повторяющие буквы в список letter

print(letters)  # список с количеством повторяющих букв, далее расшифруем список
for i in range(26):
    if letters[i] > 0:
        # print(i, letters[i])  # расшифровываем индекс буквы из словаря и сколько раз она повторяется
        # print(chr(i + 97), '=', letters[i])  # chr - перобразует 'i' обратно в букву, но для это вернем ей ее код + 97
        print(chr(i + 97) * letters[i], end='')


# Пример
print('\n Пример')
# создадим список с рандомными числами от -10 до 10 и сортируем его по тому какие числа там повторяются и сколько раз

f = []
import random

for i in range(10):
    f.append(random.randint(-10, 10))  # заполняем список случайным образом от 10 до -10

countC = [0] * 21  # создаем пустой список для посчета всех значений от -10 до 10
for i in f:
    countC[i + 10] += 1  # чтобы значение -10 превраить в индекс 0 мы будем делать +10
print(f)  # смотрим на получившийся список для сравнения
for i in range(21):
    if countC[i] > 0:
        print(i - 10, countC[i])  # преобразуем смещенные значенияобратно в оригинальные (+10) и выводим их кол-во