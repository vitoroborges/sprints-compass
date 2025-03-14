class Pessoa:
    __nome = None
    def __init__(self, id):
        self.id = id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value

pessoa = Pessoa(0)

pessoa.nome = "Fulano De Tal"

print(pessoa.nome)
