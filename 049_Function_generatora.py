# 49 Функция генератор. Создание генератора при помощи yield Python

print('функция 1')


def f():
    return [43, 65, 32]


print(f())
print(f())

print('функция 2')


# будем писать функции которые будут возвращать по односу значению

def genf():
    for i in [43, 65, 32]:
        yield i  # с помощью конструкции yield наша функция каждый раз запоминает какое значение нам возвращает
        # и какое нужно вернуть следующее


s = genf()  # к переменной 's' присваиваем результат работы функции genf()
print(s)  # мы видим что s это генератор а значит можем его обойти 1 раз
print(next(s))
print(next(s))
print(next(s))

# также с помощью этой функции мы можем выполнить итерацию
for i in genf():
    print(i)

print('функция 3')


def genff():
    ss = 7
    for i in [43, 65, 32]:
        yield i  # сдесь функция замараживается
        print(ss)
        ss = ss * 10 + 7  # затем при вызове next второй раз выводиться 7, и выводится 65 и на yield все останавливается


g = genff()

print(next(g))  # next - первый вызов
print(next(g))  # next - второй вызов

# Пример 1
print('Пример 1')


# напишем обычную функцию по нахождению факториала
def fact(n):
    pr = 1
    a = []
    for i in range(1, n + 1):
        pr = pr * i
        a.append(pr)
    return a


print(fact(10))


# а теперь перепишим этй функцию чтобы она стала гениратором

def fact1(n):
    pr = 1
    for i in range(1, n + 1):
        pr = pr * i
        yield pr


# ss = fact1(10)

for i in fact1(10):
    print(i, end=' ')  # при данной реализации наш генератор не хранит в списке результат хранения функции,
# а создает по запросу
# генераторы функций они замораживают свое выполнение до того момента когда мф не попросим продолжить с
# последнего момента
