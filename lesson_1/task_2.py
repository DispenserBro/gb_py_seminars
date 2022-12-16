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