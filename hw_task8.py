# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy: str = dd_mm_yyyy

    def __str__(self):
        return self.dd_mm_yyyy

    @classmethod
    def extract(cls, dd_mm_yyyy):
        value = []
        for i in dd_mm_yyyy.split():
            if i != '-':
                value.append(i)
        return f'Good date {int(value[0]), int(value[1]), int(value[2])}'

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Good date'
                else:
                    return f'Wrong years'
            else:
                return f'Wrong month'
        else:
            return f'Wrong day'


date = Date('18-10-2021')
print(date)
print(date.validation(18, 10, 2022))
print(date.validation(0, 12, 2021))
print(date.validation(1, 13, 2021))
print(Date.extract('18 - 10 - 2021'))
#
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.


class ExceptionClass(Exception):
    def __init__(self, errordescription):
        self.errordescription = errordescription


el1 = float(input('Enter element one: '))
el2 = float(input('Enter element two: '))


def div_el(el1, el2):
    try:
        if el2 == 0:
            raise ExceptionClass('Division by zero is forbidden')
        return print(f'Result {el1 / el2}')
    except ExceptionClass as err:
        print(err)


div_el(el1, el2)
#
# 3. Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа
# и строки. При вводе пользователем очередного элемента необходимо реализовать проверку
# типа элемента и вносить его в список, только если введено число. Класс-исключение
# должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.


class MyError(Exception):
    def __init__(self, errordescription):
        self.errordescription = errordescription


my_list = []
while True:
    try:
        el = input('Enter number or q to exit')
        if el == 'q':
            break
        if not el.isdigit():
            raise MyError(el)
        my_list.append(float(el))
    except MyError as err:
        print(f'{err} - it is not number')
print(my_list)
#
