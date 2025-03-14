def imprimir_args(*args, **Kwargs):
    for i in args:
        print(i)
        
    for key, value in Kwargs.items():
        print(value)

imprimir_args(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)