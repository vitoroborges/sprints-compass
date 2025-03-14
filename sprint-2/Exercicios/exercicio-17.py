class Calculo:
    def soma(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y
    
calculo = Calculo()

x = 4 
y = 5

print(f"Somando {x}+{y} = {calculo.soma(x, y)}")
print(f"Somando {x}-{y} = {calculo.subtracao(x, y)}")