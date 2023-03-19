# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
# Создаем переменную, в которой содержатся 3 случайные песни из  списка
# Создаем переменную new_list_1, в ней содержится сумма трех песен, время определяем по индексам
# Выводим общее время звучания трех случайных песен, срезая до двух точек после запятой для удобства восприятия
import random
new_list = random.sample(my_favorite_songs, 3, counts = None)
new_list_1 = (new_list[0][1] + new_list[1][1] + new_list[2][1])
print(f'Три песни звучат {new_list_1:.2f} минут')

# Дополнительно для пункта A
# Пункт С
# Сгенерируйте случайные песни с помощью модуля random

# Создаем переменную, в которой содержатся 3 случайные песни из  списка
# Создаем переменную new_list_2. В ней содержится название трех песен, которые определяем по индексам
import random
new_list = random.sample(my_favorite_songs, 3, counts = None)
new_list_2 = (new_list[0][0] + ', ' + new_list[1][0] + ', ' + new_list[2][0])
print(new_list_2)

# Дополнительно для пункта A 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
# Переменная x содержит в себе время трех случайных песен
# Разбиваем время на значение minuts и seconds и приводим их к целому числу
# Используем if чтобы привести время в стандартное значение до 59 сек, и +1 мин если сек > 60
# Выводим на консольб используем модуль datetime
import datetime
x = new_list_1
minuts = int(x)
seconds = int(x * 100 % 100)
if seconds > 60 :
   minuts = minuts + 1
   seconds = int(seconds - 60)
print(datetime.time(00,minuts,seconds).strftime('%M:%S'))

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# Приводим словарь к списку
# Создаем переменную, в которой содержатся 3 случайные песни из  списка
# Создаем переменную songs_time, в ней содержится сумма трех песен, время определяем по индексам
# Выводим общее время звучания трех случайных песен, срезая до двух точек после запятой для удобства восприятия
import random
playlist = list(my_favorite_songs_dict.items())
random_songs = random.sample(playlist, 3, counts = None)
songs_time = (random_songs[0][1] + random_songs[1][1] + random_songs[2][1])
print(f'Три песни звучат {songs_time:.2f} минут')

# Дополнительно для пункта B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random

import random
random_songs = random.sample(playlist, 3, counts = None)
random_somgs_1 = (random_songs[0][0] + ', ' + random_songs[1][0] + ', ' + new_list[2][0])
print(random_somgs_1)

# Дополнительно для пункта B
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import datetime
y = songs_time
minuts = int(y)
seconds = int(y * 100 % 100)
if seconds > 60 :
    minuts = minuts + 1 
    seconds = int(seconds - 60)
print(datetime.time(00,minuts,seconds).strftime('%M:%S'))
