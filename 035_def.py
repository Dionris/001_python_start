# Определение функции

def sayHello():
    print('Hello')
    print('World')
    print('and everybody')


def square(x):
    print('Квадрат числа ', x, '=', x ** 2)


def multiply(a, b):
    print(a * b)


def even(a):
    if a % 2 == 0:  # проверяем если число делиться на два
        print(a, 'четное')
    else:
        print(a, 'не четное')


def factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr = pr * i
    print(pr)


if 5 > 7:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')

# Главная программа (в ней будем вызывать функции)

sayHello()

print('pause')

sayHello()

square(3)
square(10)

for i in range(1, 11):
    square(i)

multiply(2, 5)

for i in range(20, 32):
    even(i)

factorial(3)

primer()
