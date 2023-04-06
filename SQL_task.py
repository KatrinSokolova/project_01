# Создаем таблицу Students
import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """CREATE TABLE Students (
Student_Id INTEGER NOT NULL PRIMARY KEY, 
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL
);
"""
cursor.execute(query)
connection.commit()
connection.close()

# Заполняем значениями таблицу Students
import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """INSERT INTO Students (Student_Id, Student_Name, School_Id) 
VALUES
('201', 'Иван', 1),
('202', 'Петр', 2),
('203', 'Анастасия', 3),
('204', 'Игорь', 4);
"""
cursor.execute(query)
connection.commit()
connection.close()

# Решаем задачу с взаимосвязью двух таблиц с помощью подсекции JOIN

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_detail(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name 
    FROM Students 
    JOIN School ON Students.School_Id = School.School_Id WHERE Student_Id = ?"""
    cursor.execute(select_query,(student_id,))
    records = cursor.fetchall()
    print ("Данные по ID студента")
    for row in records:
      print ("ID студента: ", row[0])
      print ("Имя студента: ", row[1])
      print ("ID школы: ", row[2])
      print ("Название школы: ", row[3])
    close_connection(connection)
  except (Exception, sqlite3.Error) as erorr:
    print ("Ошибка в получении данных", erorr)

get_student_detail(203)
