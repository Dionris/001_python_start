# Использование функции

import turtle


def move(a, b):
    turtle.forward(a)  # размер шага черепашки
    turtle.left(90)  # поворот может быть влево или вправо - (right())
    turtle.forward(b)  # размер шага черепашки
    turtle.left(90)  # поворот может быть влево или вправо - (right())


def drawSquare(a, b):
    for i in range(1 + 1):
        move(a, b)


def drawSquareColor(a, b, color):
    turtle.color(color)  # изменяем цвет иначе закраситься в черный(по умолчанию)
    turtle.begin_fill()  # начинает заполнение цвета
    drawSquare(a, b)
    turtle.end_fill()  # останавливает заполнение цветом


turtle.speed(1)  # скорость черепашки

# Вывод Результата
drawSquareColor(60, 30, 'red')
turtle.goto(150, 150)  # перемещение ее на другую координату
drawSquareColor(120, 50, 'blue')
