# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Используем input для ввода месяца
import datetime
number = input('Введите номер месяца: ')
month = int(number)

# Решаем через условные операторы
# Если введенный номер месяца < 1 или > 12, то напечатать: Такого месяца нет, и выйти
# Используем модуль datetime для вывода месяца
# Если ввели цифру 2, то дней в месяце 28
# Если ввели цифру 4,6,9,11 то дней в месяце 30
# Остальные значения - 31 день в месяце

if int(month) < 1  or int(month) > 12:
    print("Такого месяца нет!")
    quit()
month_name = datetime.date(2023, month,1).strftime("%B")
if int(month) == 2:
    days_in_month = 28
    print('Вы ввели: ', month_name,",", days_in_month, "days")
elif  int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
    days_in_month = 30
    print('Вы ввели: ', month_name,",", days_in_month, "days")
else:
    days_in_month = 31
    print('Вы ввели: ', month_name,",", days_in_month, "days")
