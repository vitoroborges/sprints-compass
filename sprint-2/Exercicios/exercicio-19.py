class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade, cor="azul"):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = cor
    
avioes = [Aviao("BOIENG456", 1500, 400), Aviao("Embraer Praetor 600", 863, 14), Aviao("Antonov An-2", 258, 12 )]

for aviao in avioes:
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima} km/h: capacidade para {aviao.capacidade} passageiros: Cor {aviao.cor}.")
