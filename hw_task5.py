import json
# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
my_file = open('ex1.txt', 'w')

while True:
    text = input('Enter text: ')
    if text == '':
        break
    else:
        my_file.writelines(text + '\n')
my_file.close()

my_file = open('ex1.txt', 'r')
content = my_file.read()
print(f'\nMy file ex1:\n{content}')
my_file.close()
#
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
my_file = open('ex2.txt', 'r')
content = my_file.read()
print(f'My file ex2:\n{content}')
my_file.close()

my_file = open('ex2.txt', 'r')
content = my_file.readlines()
print(f'Count rows: {len(content)}')
my_file.close()

num_lines = 0
num_words = 0
with open('ex2.txt', 'r') as var_file:
    for line in var_file:
        words = line.split()
        num_lines += 1
        num_words = len(words)
        print(f'Row {num_lines} words {num_words}')
#
# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
staff = {}
total = 0
count = 0
with open('ex3.txt', 'r') as my_file:
    for line in my_file:
        name, salary = line.split()
        staff[name] = salary
        if int(salary) < 20000:
            print(f'Salary less 20000 {name}')
        total += int(salary)
        count += 1
result = round(total / count, 2)
print(f'Average salary {result}')
#
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно
# данные. При этом английские числительные должны заменяться на русские. Новый блок
# строк должен записываться в новый текстовый файл.
value = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('ex4.txt', 'r') as my_file:
    for line in my_file:
        line = line.split(' ', 1)
        new_file.append(value[line[0]] + ' ' + line[1])

with open('ex4_new.txt', 'w') as my_file2:
    my_file2.writelines(new_file)

my_file3 = open('ex4_new.txt', 'r')
content = my_file3.read()
print(f'New file ex4:\n{content}')
my_file.close()
#
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
# выводить ее на экран.
with open('ex5.txt', 'w+') as my_file:
    line = input('Enter numbers through a space: ')
    my_file.writelines(line)
    el = line.split()
    print(f'Summa: {sum(map(int, el))}')
#
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все
# типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
my_dict = {}
with open('ex6.txt', 'r') as my_file:
    for line in my_file.readlines():
        value = line.replace('(', ' ').split()
        my_dict[value[0]] = sum(int(i) for i in value if i.isdigit())
print(f'Total hours for subject:\n{my_dict}')
#
# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
'''Up call function json'''
firm_prof = {}
prof_aver_dict = {}
sum_prof = 0
prof_aver = 0
i = 0
my_list = []
with open('ex7.txt', 'r') as my_file:
    for line in my_file:
        firm, ownership, profit, cost = line.split()
        firm_prof[firm] = int(profit) - int(cost)
        if firm_prof.setdefault(firm) >= 0:
            sum_prof = sum_prof + firm_prof.setdefault(firm)
            i += 1
    prof_aver = round(sum_prof / i, 2)
    prof_aver_dict = {'Average profit': prof_aver}
    my_list.append(firm_prof)
    my_list.append(prof_aver_dict)
    print(f'Result: {my_list}')

with open('ex7.json', 'w') as my_json:
    json.dump(my_list, my_json)

with open('ex7.json') as my_json:
    content = json.load(my_json)
print(f'Value in json:\n{content}')
