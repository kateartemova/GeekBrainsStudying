# 1. Создать список и заполнить его элементами различных типов
# данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка
# можно не запрашивать у пользователя, а указать явно, в программе.
var_list = [True, 0, 123, -456, 1.5, 'text', "text", '', [1, 2, 3], (1, 1.5, "Hello"), {"name": "Kate"}]

for var_el in var_list:
    el_type = type(var_el)
    print(f'{var_el} - {el_type}')

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
var_list = []
el_count = int(input('Enter count elements'))
c = 0
el = 0

while c < el_count:
    var_list.append(input('Enter an element'))
    c += 1

for var_el in range(len(var_list) // 2):
    var_list[el], var_list[el + 1] = var_list[el + 1], var_list[el]
    el += 2
print(f'New list {var_list}')

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить
# к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
season_list = ['winter', 'spring', 'summer', 'autumn']
season_dict = {
    'winter': ['12', '1', '2'],
    'spring': ['3', '4', '5'],
    'summer': ['6', '7', '8'],
    'autumn': ['9', '10', '11']
}

month = input('Enter a number month (1-12):')

if month == '1' or month == '2' or month == '12':
    print(f'In list it a {season_list[0]}')
elif month == '3' or month == '4' or month == '5':
    print(f'In list it a {season_list[1]}')
elif month == '6' or month == '7' or month == '8':
    print(f'In list it a {season_list[2]}')
elif month == '9' or month == '10' or month == '11':
    print(f'In list it a {season_list[3]}')

for var_season, var_month in season_dict.items():
    if month in var_month:
        print(f'In dict it a {var_season}')

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
var_str = str(input("Enter text"))
num = 1

for var_el in range(var_str.count(' ') + 1):
    var_word = var_str.split()
    print(f'{num} {var_word[var_el][:10]}')
    num += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый
# элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].
var_list = [7, 5, 3, 3, 2]
number = int(input('Enter new number'))
el = None

# var_list.append(number)
# new_list = sorted(var_list, reverse=True)
# print(f'New list {new_list}')

for ind, num in enumerate(var_list):
    if number > num:
        el = ind
        break
if el is None:
    var_list.append(number)
else:
    var_list.insert(el, number)
print(f'New list {var_list}')
