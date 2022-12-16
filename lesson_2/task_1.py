# Напишите программу, которая принимает на вход число N
# и выдаёт последовательность размера N из чередующихся по знаку степеней тройки

n = int(input("Enter the number of elements: "))

lst_pow = []
for i in range(n):
    lst_pow.append((-3) ** i)

print(*lst_pow, sep=' | ')