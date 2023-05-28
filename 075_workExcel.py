#  Как записывать данные в Excel


import openpyxl
import json

with open('075_movie.json') as file:
    data = json.load(file)

#print(data)  # проверяем считало ли значения
#print(type(data))  # проверяем тип (видим что это словарь)
#print(data['movies'])  # получаем список всех фильмов

for movie in data['movies']:  # распарсили словарь movies (1)
    id = movie['id']
    title = movie['title']
    year = movie['year']
    genres = movie['genres']
    director = movie['director']
    actors = movie['actors']
#    print(movie)  # распарсили словарь movies (2)
    print(id, title, year, genres, director, actors)

book = openpyxl.Workbook()  # создаем эксель файл

sheet = book.active  # выбираем лист

#sheet['A2'] = 100  # заполняем
#sheet['B3'] = 'hello'

#sheet[1][0].value = 'work'  # тут уже нужно использовать метод value для того чтобы поместить данные в ячейку

#sheet.cell(row=1,column=3).value = 'hello world'  # тут уже нужно использовать метод value для того чтобы поместить данные в ячейку


# Записываем данные Json файла в наш Excel файл
sheet['A1'] = 'ID'
sheet['B1'] = 'TITLE'
sheet['C1'] = 'YEAR'
sheet['D1'] = 'GENRES'
sheet['E1'] = 'DIRECTOR'
sheet['F1'] = 'ACTORS'

row = 2
for movie in data['movies']:  # распарсили словарь movies (1)
    sheet[row][0].value = movie['id']
    sheet[row][1].value = movie['title']
    sheet[row][2].value = movie['year']
    sheet[row][3].value = ' '.join(movie['genres'])
    sheet[row][4].value = movie['director']
    sheet[row][5].value = movie['actors']
    row += 1

book.save('075_my_book.xlsx')
book.close()
