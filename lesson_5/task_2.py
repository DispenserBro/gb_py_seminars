#* Написать программу, которая будет удалять все слова в которых есть "абв"

def remove_str(lst: list[str], key: str = 'абв') -> list:
    res_lst = []
    
    for el in lst:
        if key in el:
            continue
        res_lst.append(el)

        # if key not in el:
        #     res_lst.append(el)

    return res_lst


# print(remove_str(['привет', 'приабвет', 'приабвг'], "бвг"))

with open('strs.txt', 'r', encoding='utf-8') as f:
    lst_in = f.read().split()

print(remove_str(lst_in))
