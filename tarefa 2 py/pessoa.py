class Pessoa:
    def __init__(self, nome, numeroConta, dataAberturaConta, status):
        self.__nome = nome
        self.__numeroConta = numeroConta
        self.__dataAberturaConta = dataAberturaConta
        self.__status = status

    # Getters e Setters para nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # Getters e Setters para numeroConta
    @property
    def numeroConta(self):
        return self.__numeroConta

    @numeroConta.setter
    def numeroConta(self, numeroConta):
        self.__numeroConta = numeroConta

    # Getters e Setters para dataAberturaConta
    @property
    def dataAberturaConta(self):
        return self.__dataAberturaConta

    @dataAberturaConta.setter
    def dataAberturaConta(self, dataAberturaConta):
        self.__dataAberturaConta = dataAberturaConta

    # Getters e Setters para status
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    # Método para imprimir as informações da instância
    def imprimir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Número da Conta: {self.numeroConta}')
        print(f'Data de Abertura da Conta: {self.dataAberturaConta}')
        print(f'Status: {self.status}')
