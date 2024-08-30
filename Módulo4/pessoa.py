class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, rg, status):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg
        self.__status = status


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, nome):
        self.__nome = nome




        