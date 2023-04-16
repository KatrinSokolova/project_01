# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

class Matrix:
  def __init__(self, row, colum):
    self.row = row
    self.colum = colum
    self.matrix = [[1] * self.colum for i in range(self.row)]

  def set_value(self, i, j, value):
    if j < 0 or j >= self.colum:
        raise IndexError("Column index out of range")
    if i < 0 or i >= self.row:
        raise IndexError("Row index out of range")
    self.matrix[i][j] = value

  def get_value(self, i, j):
    if j < 0 or j >= self.colum:
        raise IndexError("Column index out of range")
    if i < 0 or i >= self.row:
        raise IndexError("Row index out of range")
    return self.matrix[i][j]

  def get_rows(self):
    return self.row

  def get_columns(self):
    return self.colum

  def __str__(self):
    s = ''
    for i in range(self.row):
        for j in range(self.colum):
            s += str(self.get_value(i, j)) + ' '
        s += '\n'
    return s


matrix = Matrix(7, 7)
print(matrix)

matrix.set_value(1, 2, 5)
print(matrix.get_value(1, 2))
print(matrix)

print(matrix.get_rows())

print(matrix.get_columns())