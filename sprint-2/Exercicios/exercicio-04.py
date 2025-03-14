items = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def eliminar_dup(items):
    nova_lista = list(set(items))
    print(nova_lista)

eliminar_dup(items)
