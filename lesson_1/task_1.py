# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого

def is_square(first_number, second_number):
    if first_number == second_number ** 2:
        print(f'{first_number} = {second_number}^2')
    elif second_number == first_number ** 2:
        print(f'{first_number}^2 = {second_number}')
    else:
        print('нет')

input_1_arg = int(input('Введите первое число: '))
input_2_arg = int(input('Введите второе число: '))

is_square(input_1_arg, input_2_arg)