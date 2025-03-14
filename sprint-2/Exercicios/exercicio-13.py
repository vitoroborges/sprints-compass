import random

random_list = random.sample(range(500), 50)

def calcular_mediana(lista):
    lista_ordenada = sorted(random_list)
    tamanho = len(lista_ordenada)
    meio = tamanho // 2

    if tamanho % 2 == 0:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        return lista_ordenada[meio]

mediana = calcular_mediana(random_list)
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")