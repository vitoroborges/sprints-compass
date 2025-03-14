palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras:
    invertido = palavra[::-1]

    if palavra == invertido:
        print(f"A palavra: {palavra} é um palíndromo\n")
    else:
        print(f"A palavra: {palavra} não é um palíndromo\n")