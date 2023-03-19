# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Вариант 1
# Считаем количество всех символов функцией len, затем выводим с помощью индексации нужную последовательность
print(len(my_favorite_songs))
print (my_favorite_songs[:14], my_favorite_songs[63:77], my_favorite_songs[15:30], my_favorite_songs[50:62])

# Вариант 2
# Считаем количество песен функцией len, разделив переменную функцией split по знаку запятой
# Затем выводим с помощью индексации нужную последовательность, также разделив переменную функцией split по знаку запятой

print(len(my_favorite_songs.split(sep = ",")))
print (my_favorite_songs.split(sep = ",")[0],
       my_favorite_songs.split(sep = ",")[4], 
       my_favorite_songs.split(sep = ",")[1],
       my_favorite_songs.split(sep = ",")[3])

