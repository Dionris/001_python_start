# 3 - Установление соответсвие между обьектами

words = {}
while True:  # установили бессконечный цикл
    s = input()
    if s == 'exit':
        break
    if s in words:
        print("Слово",s,'переводится как',words[s])
    else:
        print("Введите перевод слова",s)
#        translate = input()
#        words[s] = translate
        words[s] = input() # сокраченно верхние две строчки


