#* Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических формул нахождения корней квадратного уравнения
# D = B^2 - 4 * A * C

# def find_sol(*args):
# discr = args[1] ** 2 - 4 * args[0] * args[2]
def find_sol(coef_a, coef_b, coef_c):
    discr = coef_b ** 2 - 4 * coef_a * coef_c

    if discr < 0:
        return f'Discriminant less than zero! {discr}'
    elif discr == 0:
        return round(((-coef_b) + discr ** 0.5) / 2 * coef_a, 2)
    else:
        return [
            round(((-coef_b) + discr ** 0.5) / 2 * coef_a, 2),
            round(((-coef_b) - discr ** 0.5) / 2 * coef_a, 2)
        ]

print('Ax² + Bx + C = 0')
lst_coefs = list(map(int, input('Enter list coefficents divided by space: ').split()))

result = find_sol(*lst_coefs)

print(result)