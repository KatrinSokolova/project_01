# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

# Создаем словарь и присваивем ключам с числовым значением от 1 до 10 соответствующие значения прописью
# Создаем переменную для ввода числовых значений
# Создаю функцию в которой благодаря методу get по ключу  вызываем его значение 

numbers_dict = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight',9:'Nine'}
number_input = int(input('Введите число от 0 до 9: '))
def switch_it_up(number):
    for i in numbers_dict:
        value = numbers_dict.get(number_input)
    return value
print(switch_it_up(numbers_dict))


