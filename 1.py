"""1. Создайте словарь из пар <десятичное число>:<шестнадцатеричное
представление числа>. Десятичные числа вводятся, шестнадцатеричное
представление формируется в программе """

decimal_numbers = input("Введите числа через пробел: ")
decimal_numbers = decimal_numbers.split()
hex_dict = {}

for num in decimal_numbers:
    decimal = int(num)
    hex_dict[decimal] = hex(decimal)

print("Словарь чисел:", hex_dict)
