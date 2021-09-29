# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.
a = int(input('Enter int number a '))
b = int(input('Enter int number b '))
print('Number a', a)
print('Number b', b)
c = "Sum number ="
print(c, a + b)
d = str(input('Enter text '))
print('You enter:', d)

# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
sec = int(input('Enter seconds:'))
hours = str(sec // 3600)
minutes = str((sec // 60) % 60)
seconds = str(sec % 60)
print('You enter', sec)
print('New format hh:mm:ss', hours + ':' + minutes + ':' + seconds)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
n = int(input('Enter number n:'))
total = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print('You enter', n)
print('Result:', total)

# # 4. Пользователь вводит целое положительное число. Найдите самую большую
# # цифру в числе. Для решения используйте цикл while и арифметические операции
num = int(input('Enter positive integer:'))
new_num = 0
while num > 0:
    x = num % 10
    num //= 10
    if x > new_num:
        new_num = x
print('Big number:', new_num)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.
revenue = float(input('Enter revenue of the company:'))
costs = float(input('Enter costs of the company:'))
if revenue > costs:
    print(f'We have good result, profit: {revenue / costs:.2f}')
    staffs = int(input('Enter number staffs:'))
    print(f'Profit for one staff: {revenue / staffs:.2f}')
else:
    print('We have lesion')

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил
# a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее
# b километров. Программа должна принимать значения параметров a и b и выводить одно
# натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
a = float(input("Enter result runs first day(km):"))
b = float(input("Enter total desired result(km):"))
day = 1
while a < b:
    a *= 1.1
    day += 1
print(f"You do your task on {day} days")
