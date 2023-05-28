# *args и **kwargs Python. Передача аргументов в функцию


# *args - образует список для неименованных объектов
*a, b, c = [True, 7, 'hello', 9, '54', 67, 3, 4]  # значения '3' идет в 'b', а значение '4' идет в 'c'
print(a, b, c)

a, *b, c = [True, 7, 'hello', 9, '54', 67, 3, 4]  # все значения которые идут после значения 'True' идет в 'b' а '4'
# идет в 'c'
print(a, b, c)

a, b, *c = [True, 7, 'hello', 9, '54', 67, 3, 4]  # все значения которые идут после значения 7 идет в 'c'
print(a, b, c)

*a, b, c = 'hello world'
print(a, b, c)

*a, b, c = [2, 3]
print(a, b, c)

# еще применение '*'
s = [4, 10]
print(list(range(1, 5)))
print(list(range(*s)))  # '*' - распакует список 's' и получем последовательность от 4 до 9


# еще пример с '*'
def f(a, b, c, d):
    print(a, b, c, d)


f(1, 2, 3, 4)
a = ('hello', True, 78, [3, 4, 5])

f(*a)  # '*' - распакует наши 4 значения в переменной 'a'


# еще пример с '*'
def ff(*args):  # '*' - можем передать в нашу функцию неопределенное кол-во неименованных аргументов
    s = 0
    for i in args:
        s += i
    # print(args, type(args))  # args - тут уже образует кортеж!!!
    return s


print(ff(1, 2, 3, 4, 5, 6, 7))


# ff(1, 2, 3, 4, 5, 6, 7, 8)
# ff(2,3)
# ff()


# **Kwargs - для именованных объектов
def fff(**kwargs):
    print(kwargs)
    for k, w in kwargs.items():
        print(k, w)


fff(a=1, b=2, c=6, name=89)  # **Kwargs - превращается в словарь


# также можно комбинировать 2 способа '*' и '**'
def ffff(*args, **kwargs):
    print(args, kwargs)
    # for k, w in kwargs.items():
    #     print(k, w)


ffff(2, 3, 4, 5, 2, 5, 7, a=1, b=2, c=6, name=89)  # *args - превращается в кортеж, **Kwargs - превращается в словарь


# еще пример
def outPrint(*args, sep='#', end='@'):
    print(args, sep, end)


outPrint(1, 2, 3, 4, 5, 6, sep='90')
outPrint(1, 2, end=111)
outPrint(1, 2)

# print(1,2,3,4,5,43,sep=' ',end=' ')


abb = [1, 2, 2, 3, 4, 5, 5]
print(abb)
print(*abb)  # произойдет распаковка списка на несколько значений, вывидет как 'print(1, 2, 2, 3, 4, 5, 5)'
print(1, 2, 2, 3, 4, 5, 5)

print(1, 2, 3, 4, 5, 6, sep='o', end='r')
