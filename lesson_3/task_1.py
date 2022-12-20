#* Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def find_value(lst: list, value) -> bool:
    # value1 = None
    # if type(value) == str and value.isdigit():
    #     value1 = int(value)

    for item in lst:
        # if item == value or (value1 and item == value1):
        if item == value:
            return True

    return False


lst_in = [1, 2, 3, 4]

item_to_search = 1

is_found = find_value(lst_in, item_to_search)

print(is_found)
