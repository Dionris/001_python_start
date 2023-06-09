# Передача аргументов Python. Сопоставление аргументов по имени и позиции

def f(a, b):
    print(id(a), id(b), 'local')
    a = 100
    b.append(100)  # изменяем переменную 'b'
    b[1] = 'hi'  # изменяем переменную 'b'
    print(id(a), id(b), 'local after')  # id 'c' и 'd' будут совпадать с id 'a' и 'b' до присваивания внутри функции
    print(a, b, 'local')


c = 'hello'  # не изменяемая переменная
d = [1, 2, 3, 4, 76]  # изменяемая переменная
print(id(c), id(d), 'global')  # id 'c' и 'd' будут совпадать с id 'a' и 'b' до присваивания внутри функции

# f(c, d)  # переменная 'd' измениться из-за функции
# print(c, d, 'global')

f(c, d[:])  # переменная 'd' не измениться потомучто в нутри функции мы делаем все действия над копией этого списка,
# так как передали копию списка 'd' при помощю полного среза [:],
print(c, d, 'global')

# Пример
print('\nПример')


def ff(aa, bb, cc):
    print(aa, bb, cc)


# позиционный
ff(1, 5, 7)

# по имени
ff(bb=10, cc=20, aa=5)

# комбинированный вариант
ff(1, cc=4, bb=3)


# можем присвоить значения по умолчанию
def fff(aaa='HI', bbb='Hello', ccc='неизвестно'):
    print(aaa, bbb, ccc)


fff()
fff(1)
fff(2, 3)
fff(2, 3, 4)
fff(bbb=101)
