# 2 - Замена разряженного списка

r = input()
a = {}
for i in r:
    if i.isalpha():
        a[i] = a.get(i,0) + 1
print(a)  # мы выводим в словарь только те элементы которые исползуем а не используеммые буквыв как ноль не записываются чтобы не тратить память


