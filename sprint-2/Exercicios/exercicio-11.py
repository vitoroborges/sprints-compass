lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def slice_list(lista):
    size = len(lista)
    chunk = size // 3
    print(lista[:chunk], lista[chunk:2*chunk], lista[2*chunk:])

slice_list(lista)
