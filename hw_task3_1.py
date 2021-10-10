# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую
#  их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации
#  деления на ноль.
def div_el():
    try:
        el1 = float(input('Enter element one: '))
        el2 = float(input('Enter element two: '))
        result = el1 / el2
    except ZeroDivisionError:
        return 'Wrong elements, we have zero'

    return result


print(f'Result: {div_el()}')
#
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.
var_name = input('Enter name: ')
var_surname = input('Enter surname: ')
var_year = input('Enter year: ')
var_city = input('Enter city: ')
var_email = input('Enter email: ')
var_phone = input('Enter phone: ')


def data_user(name, surname, year, city, email, phone):
    return ''.join(['Name - ', name, ' Surname - ', surname, ' Year - ', year,
                    ' City - ', city, ' Email - ', email, ' Phone - ', phone])


print(data_user(name=var_name, surname=var_surname, year=var_year, city=var_city, email=var_email, phone=var_phone))
#
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3], reverse=True)[:2])


def my_func2(*args):
    return sum(sorted(list(args), reverse=True)[:2])


print(my_func(19, 2, 1))
print(my_func2(1, 2, 19))
#
# 4. Программа принимает действительное положительное число x и целое отрицательное
# число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо
# реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись
# без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
# с помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.


def my_func(x, y):
    var1 = x ** y
    var2 = 1
    i = 1
    while i <= abs(y):
        var2 *= x
        i += 1
    return var1, 1 / var2


print(f'Result: {my_func(float(input("Enter positive number x: ")),int(input("Enter int negative number y: ")))}')
#
# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.


def sum_el():
    total = 0
    symbol = 0
    while symbol == 0:
        element = input('Enter elements or symbol @: ').split()
        result = 0
        for el in range(len(element)):
            if element[el] == '@':
                symbol = 1
                break
            else:
                result = result + int(element[el])
        total = total + result
        print(f'Summa: {total}')
    print(f'Total sum: {total}')


sum_el()

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например,
# print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func():
    word = input('Enter words: ')
    print(word.title())
    return


int_func()