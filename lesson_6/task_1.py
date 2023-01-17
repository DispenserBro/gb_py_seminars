#* Напишите программу вычисления арифметического выражения заданного строкой. 
#* Используйте операции +,-,/,*. приоритет операций стандартный

# 11 / 33 - 22 * 3 / 2
#   1  4  2 3
def process_step(lst_in: list):
    if ('/' in lst_in) or ('*' in lst_in):
        for i in range(len(lst_in)):
            if lst_in[i] == '/':
                temp = lst_in[i - 1] / lst_in[i + 1]
                # del lst_in[i-1 : i+2]
                lst_in.pop(i - 1)
                lst_in.pop(i - 1)
                lst_in.pop(i - 1)
                lst_in.insert(i - 1, temp)
                break

            elif lst_in[i] == '*':
                temp = lst_in[i - 1] * lst_in[i + 1]
                lst_in.pop(i - 1)
                lst_in.pop(i - 1)
                lst_in.pop(i - 1)
                lst_in.insert(i - 1, temp)
                break
    else:
        for i in range(len(lst_in)):
            if lst_in[i] == '+':
                temp = lst_in[i - 1] + lst_in[i + 1]
                lst_in.pop(i - 1)
                lst_in.pop(i - 1)
                lst_in.pop(i - 1)
                lst_in.insert(i - 1, temp)
                break

            elif lst_in[i] == '-':
                temp = lst_in[i - 1] - lst_in[i + 1]
                lst_in.pop(i - 1)
                lst_in.pop(i - 1)
                lst_in.pop(i - 1)
                lst_in.insert(i - 1, temp)
                break

    return lst_in

def process_func(values: str):
    res_str = ''

    for el in values:
        if el.isdigit():
            res_str += el

        else:
            res_str += f' {el} '

    res_str = res_str.split()

    for i in range(len(res_str)):
        if res_str[i].isdigit():
            res_str[i] = int(res_str[i])

    count = 0
    for el in res_str:
        if type(el) == str:
            count += 1

    for _ in range(count):
        res_str = process_step(res_str)

    # return eval(values)
    return res_str[0]

print(process_func('-1100/25-22*3/2+120*8'))