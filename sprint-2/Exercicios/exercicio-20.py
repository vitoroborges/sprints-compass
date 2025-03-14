f =  open('number.txt', 'r')

numeros = map(int, f.readlines())

pares = list(filter(lambda a: a % 2 == 0, numeros))

maiores_pares = sorted(pares, reverse=True)[:5]

print(maiores_pares)

print(sum(maiores_pares))