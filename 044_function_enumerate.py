#  Функция enumerate()

a = [10, 20, 30, 40, 50, 60]  # создаем коллекцию ввиде списка
s = 'hello'  # создаем коллекцию ввиде строки
t = ('apple', 'banana', 'mango')  # создаем коллекцию ввиде кортежа
d = {'a': 1, 'b': 2, 'c': 3}  # создаем коллекцию ввиде словаря

print(enumerate(a))  # получается обьект
print(list(enumerate(a)))  # превращаем его в список и видим что внутри списка пары из кортежей

for para in enumerate(a):  # любую коллекцию можно обходить в цикле for
    print(para)  # и выводим пары

for index, value in enumerate(a):  # видим что каждый элемент представляет собой пару, то мы можем вывести знач отдельно
    print(index, value)

for index, value in enumerate(a):
    if value % 20 == 0:  # выведим только те значения которые делятся на 20
        print(index, value)

print(a)  # при изменении значения 'value' наши значения в списке 'a' не меняются

for index, value in enumerate(a):
    a[index] += 1  # чтобы изменить значения придется обращаться к элементам по индексу

print(a)

for index, value in enumerate(s):
    print(index, value)

for index, value in enumerate(t):
    print(index, value)

for index, value in enumerate(d):
    print(index, value)

# range
for index, value in enumerate(range(10, 20)):  # также можем передавать и функцию 'range()'
    print(index, value)

# Можем изменить стартовый индекс
for index, value in enumerate(t, 10):  # начнем с 10
    print(index, value)

