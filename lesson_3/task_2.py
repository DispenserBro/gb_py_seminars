#* Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет

def find_value(lst: list, value) -> int:
    count_in = 0
    indx = -1

    if lst:
        while count_in < 2 and indx < len(lst):
            indx += 1

            if lst[indx] == value:
                count_in += 1

    # for i in range(len(lst)):
    #     if lst[i] == value:
    #         count_in += 1

    #     if count_in == 2:
    #         break

    if count_in != 2:
        return -1

    # return i
    return indx


lst_in = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]

item_to_search = "йцу"

print(find_value(lst_in, item_to_search))