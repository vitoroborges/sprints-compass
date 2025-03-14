class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        print("Emitindo som...")

class Pato(Passaro):
    def emitir_som(self):
        print("Pato emitindo som...\nQuack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...\nPiu Piu")

pato = Pato()
pardal = Pardal()

pato.voar()
pato.emitir_som()

pardal.voar()
pardal.emitir_som()