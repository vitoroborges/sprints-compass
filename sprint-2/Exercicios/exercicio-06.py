a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def power_of(number):
    return number ** 2

def my_map(lista, f):
    b = list()
    for i in lista:
        b.append(f(i))
    print(b)

my_map(a, power_of)

