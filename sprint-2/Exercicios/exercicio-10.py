def sum_string(string_numeros):
    numeros = map(int, string_numeros.split(','))
    return sum(numeros)

print(sum_string("1,3,4,6,10,76"))