# 43 Рекурсивный обход файлов Python

import os  # стандартная библиотека для обхода файлов

path = "D:\\MoviesPyCharm"  # Переменная с путем к файлу


def obhodFile(path, level=1):  # создаем функцию в которой путь к нашей корневой папки и вторая переменная для удобства
    # показывает уровень вложенности
    print('level=', level, 'content=', os.listdir(path))  # принтуем наше место положение и лвл
    for i in os.listdir(path):  # перебираем элементы нашей начальной папки
        if os.path.isdir(path + '\\' + i):  # если это папка, то входим дальше (проверяем папка ли это, если не папка
            # то пропускаем)
            print('Спускаемся', path + '\\' + i)  # выше мы выявили что это папка, а тут выводим это на экран
            obhodFile(path + '\\' + i, level + 1)  # тут опять запускаем нашу функцию чтобы проверить есть ли папки в
            # этой папке, и выполняем по порядку выше действия
            print('Возвращаемся в', path)  # выводим это сообщение когда мы дошли до самого низа вложенности и когда
            # не осталось папок. В случаи когда мы обойдем все папки и файлы 'path' мы просто будем выходить до того
            # момента пока не дойдем до корня - path и тогда наша функция закончит свое выполнение


obhodFile(path) # запускаем нашу функцию


print('\nПример - работы библиотеки "os"\n')
print(os.listdir(path))  # показывает все содержимое пути в виде списка благодаря функции - listdir()
for i in os.listdir(path):
    print(i, type(i), path + '\\' + i, os.path.isdir(path + '\\' + i))  # os.path.isdir(путь) - проверяем является ли
    # папкой, "path + '\\' + i" - находим путь к файлу
    # os.path.isfile(путь) - будет проверять на файл