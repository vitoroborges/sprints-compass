import csv

notas = []
estudantes = []

with open('estudantes.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for li in csvreader:
        nome = li[0]
        notas = list(map(lambda x: int(x), li[1:]))

        maiores = sorted(notas, reverse=True)[:3]

        media = round(sum(maiores) / 3 , 2)

        estudantes.append((nome, maiores, media))
    
    estudantes_ordem = sorted(estudantes, key= lambda x: x[0])

    for estudante in estudantes_ordem:
        nome, maiores, media = estudante
        print(f"Nome: {nome} Notas: {maiores} Média: {media}")
        
