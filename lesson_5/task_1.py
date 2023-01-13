#* В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

def get_missing(lst: list[int]):
    # for i in range(1, len(lst)):
    #     if lst[i] - 1 != lst[i - 1]:
    #         return lst[i - 1] + 1
    n = len(lst) - 1
    while (lst[n] - 1 == lst[n - 1]):
        n -= 1
    return lst[n] - 1


with open('numbers.txt', 'r') as f:
    lst_in = list(map(int, f.read().split()))


print(get_missing(lst_in))