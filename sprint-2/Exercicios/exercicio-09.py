class Lampada:
    def __init__(self, ligada = False):
        self.ligada = ligada

    def liga(self):
        self.ligada = True
    
    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        isLigada = True if self.ligada == True else False
        return isLigada

lampada = Lampada()

lampada.liga()

print(f"A lampada está ligada? {lampada.esta_ligada()}")

lampada.desliga()

print(f"A lampada está ligada? {lampada.esta_ligada()}")