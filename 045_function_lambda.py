# Функция Lambda

# Схема обычной функции:
def f(x):
    return x ** 2


print(f(4))

# Схема lambda:
# lambda арг1, арг2,... : выражение

r = lambda x: x ** 2
# lambda используется в том случае когда нужно выполнить одно выражение и функция записывается в одну строчку

print(r(7))

# Пример 1
print('\n Пример 1:')


# 1
def perimetr(a, b, c):
    return a + b + c


# 2
per = lambda a, b, c: a + b + c
# мы можем использовать lambda вместо обычной функции когда в обычной функции есть 'return'
# с помощью lambda нельзя реализовать функции в которых есть циклы

# 1
print(perimetr(1, 2, 3))
# 2
print(per(1, 2, 3))

# Пример 2
print('\n Пример 2:')

h = lambda: 'Hello'  # мы можем и не класть никаких аргументов

print(h())

# Пример 3
print('\n Пример 3:')


def g(x):
    return x % 10


v = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
v.sort(key=g)
print(v)


def g(x):
    return x % 10


v.sort(key=lambda x: x % 10)  # x%10 - по последней цифре
print(v)

v.sort(key=lambda x: x // 10 % 10)  # x//10%10 - по предпоследней цифре ( у 8 переди 0)
print(v)


# Пример 4
print('\n Пример 4:')

def linear(k,b):
    return lambda x: x*k +b

graf1 = linear(2,5)
print(graf1(3))

graf2 = linear(-4,1)
print(graf2(5))
