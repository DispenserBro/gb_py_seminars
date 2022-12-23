#* Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Без min и max

def max_min(lst: list) -> list: # ->
    if not lst:
        return []

    min_value = lst[0]
    max_value = lst[0]

    # for i in range(len(lst)):
    #     if lst[i] < min_value:
    #         min_value = lst[i]

    #     if lst[i] > max_value:
    #         max_value = lst[i]

    for el in lst:
        if el < min_value:
            min_value = el

        if el > max_value:
            max_value = el

    return [max_value, min_value]


lst_in = list(map(int, input('Enter list els divided by space: ').split()))

result = max_min(lst_in)

print('Maximal and minimal vaues:', *result, sep=' ')
