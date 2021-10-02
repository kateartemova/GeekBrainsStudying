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
var_list = []

while True:
    el = int(input('Enter new number: '))
    if el <= 0:
        break
    if len(var_list) > 0:
        if el <= var_list[-1]:
            var_list.append(el)
            print(var_list)
        else:
            for ind in range(len(var_list)):
                if el >= var_list[ind]:
                    var_list.insert(ind, el)
                    print(var_list)
                    break
    else:
        var_list.append(el)
        print(var_list)
print(var_list)
print(f'New list {var_list}')

# 6. * Реализовать структуру данных «Товары». Она должна представлять
# собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
# ключ — характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
products = []
analitics = {'Name': [], 'Price': [], 'Count': [], 'Units': []}

num = 1
while True:
    if input("You want to add product? (enter y/n)").lower() == 'y':
        name = input('Name: ')
        price = input('Price: ')
        count = input('Count: ')
        units = input('Units: ')

        products.append((num, {'Name': name, 'Price': price, 'Count': count, 'Units': units}))
        num += 1
    else:
        break

for item in products:
    tmp_name_list = analitics['Name']
    tmp_name_list.append(item[1]['Name'])
    analitics['Name'] = list(set(tmp_name_list))

    tmp_price_list = analitics['Price']
    tmp_price_list.append(item[1]['Price'])
    analitics['Price'] = list(set(tmp_price_list))

    tmp_count_list = analitics['Count']
    tmp_count_list.append(item[1]['Count'])
    analitics['Count'] = list(set(tmp_count_list))

    tmp_units_list = analitics['Units']
    tmp_units_list.append(item[1]['Units'])
    analitics['Units'] = list(set(tmp_units_list))

print(f'Analytics {analitics}')
