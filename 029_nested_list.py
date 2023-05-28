a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, [4, 5, 7, 11], 17, 19]]
b = ['hello', 'hi', 'world']
c = [[0, 2, 4, 6],
     [1, 5, 9, 13],
     [3, 10, 17, 19]
     ]

print(len(a))
print(a[2][3])  # чтобы обратиться к элементу списка в списке, нужно исльзовать двойную инденсацию
print(a[0][3])  # выводим 6
print(a[2])
print(a[2][2][1])  # берем 5

print(b[2])
print(b[2][1])  # можем доставать из слов буквы
print(b[2][-1])  # можем доставать из слов буквы

for i in c:
    print(i)


# Первый вариант обхода списка
for i in c:
    for j in i:
        j += 10  # просто увеличиваем все значения j на 10, чтобы увидеть что сам список в итоге не изменился
        print(j, end=' ')
    print()
print(c)  # список не изменился потомучто мы обходили не по индексам


# Второй вариант, обход по индексам
for i in range(3):
    for j in range(4):
        c[i][j] += 10  # для проверки изменения самих эл в сиспе при обходе
        print(c[i][j], end=' ')
    print()

print(c)  # проверка того что список изменился


# меняем местами обход
for j in range(4):
    for i in range(3):
        print(c[i][j], end=' ')
    print()

# и обходим задон на перед
for i in range(2,-1,-1):
    for j in range(3,-1,-1,):
        print(c[i][j], end=' ')
    print()

# находим сумму
for i in range(2,-1,-1):
    s=0
    for j in range(3,-1,-1):
        s+=c[i][j]
    print(s)


# наполнение списка
d = []
n = int(input())  # строка
m = int(input())  # столб

for i in range(n):
    d.append([0]*m)
for i in d:
    print(i)

# заполняем список значениями
for i in range(n):
    f=[]
    for i in range(m):
        f.append(int(input()))
    d.append(f)
for i in d:
    print(i)


# Пример , делаем матрицу в которой по главной диагонали будет 10 , сверху 5, а с низу 3
print('последний пример')
h = []
k = int(input()) #строка и столбец
for i in range(k):
    h.append([0]*k) # заполняем матрицу нулями

for i in h:
    print(i) # проверяем

for i in range(k):
    for j in range(k):
        if i==j:
            h[i][j] = 10
        elif i>j:
            h[i][j] = 3
        else:
            h[i][j] = 5
for i in h:
    print(i)