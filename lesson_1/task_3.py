# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

num_n = abs(int(input('Введите число N: ')))

lst_nums = [i for i in range(-num_n, num_n + 1)]
lst_nums = list(range(-num_n, num_n + 1))

print(*lst_nums, sep=', ')