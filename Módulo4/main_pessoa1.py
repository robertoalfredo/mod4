# Importando a classe Pessoa do módulo pessoa.py
from pessoa import Pessoa

# Instanciando um objeto da classe Pessoa
pessoa1 = Pessoa("João", "2000-01-01", "000.111.222-33", "15975388-1", False)

# Imprimindo os valores iniciais dos atributos
print(f'Nome: {pessoa1.nome}')
print(f'Data de Nascimento: {pessoa1.data_nascimento}')
print(f'CPF: {pessoa1.cpf}')
print(f'RG: {pessoa1.rg}')
print(f'Status: {pessoa1.status}')

# Alterando os valores dos atributos via setters
pessoa1.nome = "Ana"
pessoa1.data_nascimento = "1995-05-05"
pessoa1.rg = "987654321-0"
pessoa1.status = True

# Tentando atribuir um CPF com menos de 14 caracteres
try:
    pessoa1.cpf = "000.111.222"  # CPF inválido
except ValueError as e:
    print(e)

# Ajustando o CPF para o valor correto de 14 caracteres
pessoa1.cpf = "123.456.789-00"

# Imprimindo os novos valores dos atributos
print(f'Nome: {pessoa1.nome}')
print(f'Data de Nascimento: {pessoa1.data_nascimento}')
print(f'CPF: {pessoa1.cpf}')
print(f'RG: {pessoa1.rg}')
print(f'Status: {pessoa1.status}')
