vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def conta_vogais(texto: str) -> int:
    return len(list(filter(lambda char: char in vogais, texto)))

