from random import randint

# Шеренга учеников отсортирована по уменьшению роста. Определить, куда в шеренгу поставить нового ученика

lst_stud = [randint(150, 250) for _ in range(10)]

lst_stud.sort()
# lst_stud.reverse()
lst_stud = lst_stud[::-1]

new_stud = int(input('Enter the height of new student: '))

print(lst_stud, new_stud, sep='\n')

for i in range(len(lst_stud)):
    if new_stud > lst_stud[i]:
        lst_stud.insert(i, new_stud)
        break

print(lst_stud)