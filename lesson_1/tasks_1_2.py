# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого

# def is_square(first_number, second_number):
#     if first_number == second_number ** 2:
#         print(f'{first_number} = {second_number}^2')
#     elif second_number == first_number ** 2:
#         print(f'{first_number}^2 = {second_number}')
#     else:
#         print('нет')

# input_1_arg = int(input('Введите первое число: '))
# input_2_arg = int(input('Введите второе число: '))

# is_square(input_1_arg, input_2_arg)

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них

def find_max(lst_nums):
    max_num = lst_nums[0]

    for number in lst_nums:
        if number > max_num:
            max_num = number

    return max_num

lst_in = []

number_els = int(input('Введите количество элементов: '))

for i in range(number_els):
    lst_in.append(int(input(f'Введите {i+1} элемент: ')))

print(find_max(lst_in))
