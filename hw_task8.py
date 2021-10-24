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
# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
# оргтехники на склад и передачу в определенное подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.


class StoreOfficeEquipment:
    def __init__(self, store_num):
        self.store_num = store_num
        self.accept_lists = {}
        self.give_out_lists = {}

    def to_accept(self, equipment):
        self.accept_lists.update({equipment.name: [equipment.price, equipment.quantity, equipment.serial_number]})
        print(f'Accept equipment: {self.store_num} {equipment.name} {equipment.price} '
              f'{equipment.quantity} {str(equipment.serial_number)}')

    def to_give_out(self, equipment, other):
        self.give_out_lists.update({equipment.name: [equipment.price, equipment.quantity, equipment.serial_number]})
        print(f'Give out equipment: {self.store_num} {equipment.name} {equipment.price} '
              f'{equipment.quantity} {str(equipment.serial_number)}')
        other.to_accept(equipment)

    def list_equipments(self):
        print(f'Accepted at the warehouse {len(self.accept_lists)} position:\n{self.accept_lists}')
        print(f'Gived out from the warehouse {len(self.give_out_lists)} position:\n{self.give_out_lists}')


class OfficeEquipment:
    def __init__(self, name, price, quantity, serial_number):
        self.name = name
        self.quantity = quantity
        self.serial_number = serial_number
        if price <= 0:
            raise ValueError('Wrong price')
        else:
            self.price = price

    def __str__(self):
        return str(self.name)


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, serial_number, print_speed):
        super().__init__(name, price, quantity, serial_number)
        OfficeEquipment.__init__(self, name, price, quantity, serial_number)
        self.print_speed = print_speed

    def __str__(self):
        return 'Model: ' + OfficeEquipment.__str__(self) + ' Print speed: ' + str(self.print_speed)


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity, serial_number, resolution):
        OfficeEquipment.__init__(self, name, price, quantity, serial_number)
        self.resolution = resolution

    def __str__(self):
        return 'Model: ' + OfficeEquipment.__str__(self) + ' Resolution: ' + str(self.resolution)


class Copier(OfficeEquipment):
    def __init__(self, name, price, quantity, serial_number, color_printing):
        OfficeEquipment.__init__(self, name, price, quantity, serial_number)
        self.color_printing = color_printing

    def __str__(self):
        return 'Model: ' + OfficeEquipment.__str__(self) + ' Color printing: ' + str(self.color_printing)


store1 = StoreOfficeEquipment('Store 1')
store2 = StoreOfficeEquipment('Store 2')
pr_1 = Printer('HP', 150, 20, 12345, '80–100 мм/с')
pr_2 = Printer('HP', 130, 20, 54321, '150 мм/с')
sc_1 = Scanner('Canon', 200, 10, 23456, '600 dpi')
c_1 = Copier('Xerox', 1000, 2, 34567, 'black-white')

print(pr_1)
print(pr_2)
print(sc_1)
print(c_1)
print('--------------------')
store1.to_accept(pr_1)
store2.to_accept(pr_2)
store1.to_accept(sc_1)
store2.to_accept(c_1)
print('--------------------')
store1.to_give_out(sc_1, store2)
store2.to_give_out(c_1, store1)
print('--------------------')
store1.list_equipments()
print('--------------------')
store2.list_equipments()
#
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных
# чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.


class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 'x + i*y'

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return ComplexNumber(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)

    def __str__(self):
        return f'z = {self.x} + i*{self.y}'


a = ComplexNumber(2, 3)
b = ComplexNumber(5, -4)
print(a)
print(a + b)
print(a * b)
