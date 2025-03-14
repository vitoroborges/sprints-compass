from functools import reduce

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

def calcula_saldo(lancamentos) -> float:   
    valores = map(lambda x: x[0] if x[1] == "C" else -x[0], lancamentos)
    saldo_final = reduce(lambda conta, x: conta + x, valores, 0)
    return saldo_final

print(calcula_saldo(lancamentos))