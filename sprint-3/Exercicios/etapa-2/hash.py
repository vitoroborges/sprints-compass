import hashlib

while True:

    print("Insira uma palava para gerar o hash (ou 'exit' para sair): ")
    x = str(input())

    if x.lower() == "exit":
        break

    if isinstance(x, str):
        hash_object = hashlib.sha1()
        hash_object.update(x.encode("utf-8"))
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
    else:
        print("Não é uma string!")