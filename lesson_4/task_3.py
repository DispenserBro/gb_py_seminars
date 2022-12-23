#* Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел

def find_nok(num_1, num_2):
    nok = max(num_1, num_2)

    if not num_1 or not num_2:
    # if num_1 == 0 or num_2 ==0: 
        # return nok
        return -1

    while nok % num_1 or nok % num_2:
    # while nok % num_1 != 0 or nok % num_2 != 0:
        nok += 1

    return nok

number_a = int(input('Enter first number: '))
number_b = int(input('Enter second number: '))

print(find_nok(number_a, number_b))