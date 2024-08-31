from pessoa import Pessoa
from pessoafisica import PessoaFisica
from pessoajuridica import PessoaJuridica

# Instanciando um objeto da classe Pessoa
pessoa = Pessoa("João", "123456", "2022-01-01", True)
pessoa.imprimir_informacoes()

# Instanciando um objeto da classe PessoaFisica
pessoa_fisica = PessoaFisica("Ana", "654321", "2023-01-01", True, "1990-05-15", "123.456.789-00", "987654321")
pessoa_fisica.imprimir_informacoes()

# Instanciando um objeto da classe PessoaJuridica
pessoa_juridica = PessoaJuridica("Empresa X", "789123", "2021-01-01", True, "2021-02-02", "12.345.678/0001-00")
pessoa_juridica.imprimir_informacoes()

# Alterando os valores dos atributos via setters
pessoa.nome = "Carlos"
pessoa.numeroConta = "111222"
pessoa.dataAberturaConta = "2020-01-01"
pessoa.status = False

pessoa_fisica.nome = "Bruno"
pessoa_fisica.numeroConta = "222333"
pessoa_fisica.dataAberturaConta = "2022-05-05"
pessoa_fisica.status = False
pessoa_fisica.cpf = "987.654.321-00"  # CPF com 14 caracteres

pessoa_juridica.nome = "Empresa Y"
pessoa_juridica.numeroConta = "333444"
pessoa_juridica.dataAberturaConta = "2021-12-12"
pessoa_juridica.status = True
pessoa_juridica.cnpj = "98.765.432/0001-00"  # CNPJ com 18 caracteres

# Imprimindo os novos valores após a modificação
print("\nApós as alterações:\n")
pessoa.imprimir_informacoes()
pessoa_fisica.imprimir_informacoes()
pessoa_juridica.imprimir_informacoes()
