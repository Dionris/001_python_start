# Возвращаемое значение функции. Оператор return Python

# Встроенные функции
a = abs(-7)  # отбрасывает знак
b = max(4, 5, 6, 3, 6, 7, 3, 5, 1)  # возвращает самое большое значение
с = max(4, 3, 5, 6, abs(-90), 80, min(100, 200))  # встроенные функции могут быть внутри функций
print(a)
print(b)
print(с)


# Cамописные функции
def square(x):
    print(x ** 2)
    # return None - это автоматически указано после каждой функции, если не написать самому


d = square(6)

print(d)


# 36
# None - каждая функция в питоне что-то возвращает, если "return" не указан, то будет возвращать None

# Перепишем функцию
def square2(x):
    return x ** 2


e = square2(square2(3))
print(e)


# Пример
def exempole():
    print(1)
    print(2)
    return 'Hello'  # return в функции работает как breack в цикле, после него ничего не работает(происходит
    # автоматический выход из функции). Может быть только один return иначе до остальных очередь не дойдет
    print(3)
    print(4)


exempole()
print(exempole())  # чтобы увидеть Hello


# Пример - проверяем четное ли число или нет
def even(x):
    return x % 2 == 0  # 3 вариант
    # if x % 2 == 0: # 2 вариант
    #     return True # 2 вариант
    # else: # 1 вариант
    #     return False # 1 вариант
    # return False  # 2 вариант


for i in range(1, 11):
    print(i, even(i))


# Пример - функция число сочетания "n" к "k"
def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    # print(pr) # раньше мы делали так
    return pr  # теперь будем возвращать резульат без вывода


# проверяем наождения факториала 8
# for i in range(1,8):
# print(i,factorial(i))

def sochet(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


print(sochet(5, 3))

# Пример
def sqAndPer(a,b):
    # return  a*b, 2*(a+b) # результат вернется в виде кортежа # 1 вариант
    mas = []
    mas.append(a*b)
    mas.append(2*(a+b))
    return mas # результат уже вернется в виде списка


# print(sqAndPer(3,6),type(sqAndPer(3,6))) # 1 вариант

# вспоминаем множественное присвоение
# square3, perimetr = sqAndPer(2,5) # 1 вариант
# print(square3,perimetr) # 1 вариант

print(sqAndPer(2,6))
