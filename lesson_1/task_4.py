# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа

# Вариант 1
input_number = float(input('Введите число: '))

if input_number % 1:
    print(int(input_number * 10 % 10))
else:
    print('нет')

# Вариант 2
# input_number_2 = input('Введите дробное число: ')

# drob_part = input_number_2.split('.')[1]

# if len(drob_part) > 1 or int(drob_part):
#     print(drob_part[0])
# else:
#     print('нет')