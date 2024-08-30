from pessoa import Pessoa

pessoa = Pessoa(nome="Joao", data_nascimento="01/01/2000", cpf="000.111.222-33", rg="15975388-1", status=False)
Pessoa.alterarstatus(True)
print(f'Nome: {Pessoa.nome}')
print(f'Data de Nascimento: {Pessoa.data_nascimento}')
print(f'CPF: {Pessoa.cpf}')
print (f'RG: {Pessoa.rg}')

Pessoa.alterarstatus(False)
print('Após alterar status para False: ')
print(f'Nome: {Pessoa.nome}')
print(f'Data de Nascimento: {Pessoa.data_nascimento}')
print(f'CPF: {Pessoa.cpf}')
print(f'RG: {Pessoa.rg}')




