from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, status, dataAberturaEmpresa, cnpj):
        super().__init__(nome, numeroConta, dataAberturaConta, status)
        self.__dataAberturaEmpresa = dataAberturaEmpresa
        self.__cnpj = cnpj

    # Getters e Setters para dataAberturaEmpresa
    @property
    def dataAberturaEmpresa(self):
        return self.__dataAberturaEmpresa

    @dataAberturaEmpresa.setter
    def dataAberturaEmpresa(self, dataAberturaEmpresa):
        self.__dataAberturaEmpresa = dataAberturaEmpresa

    # Getters e Setters para cnpj
    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        if len(cnpj) != 18:
            raise ValueError("O CNPJ deve conter 18 caracteres (no formato 00.000.000/0001-00).")
        self.__cnpj = cnpj
