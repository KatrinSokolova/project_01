
import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = """SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, School.School_Name 
    FROM Students 
    JOIN School ON Students.School_Id = School.School_Id; 
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