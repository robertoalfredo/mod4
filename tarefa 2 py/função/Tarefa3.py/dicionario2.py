md = {
    1: {'nome': 'Cristina', 'idade': 26, 'nacionalidade': 'brasileira'}
}
md.update({
    2: {'nome': 'Marcio', 'idade': 19, 'nacionalidade': 'brasileiro'},
    3: {'nome': 'Messi', 'idade': 36, 'nacionalidade': 'argentino'}
})
# Adicionando dois novos elementos ao primeiro dicionário com o comando "update"
print(md)

dicio = md.copy()
# Criando um novo dicionário e copiando o dicionário do primeiro, em cima do já criado.

md.pop(2)
print(md)
# O comando "pop" serve para excluir um elemento do dicionário, Ex: (2)

md.popitem()
print(md)
# O comando "popitem" serve para excluir o último elemento do dicionario.

md.clear()
dicio.clear()
print(md)
# Excluindo tudo dos dois dicionários com o comando "Clear"

# Usando fromkeys para criar um novo dicionário
chaves = ['a', 'b', 'c']
valor_padrao = 0
novo_dicionario = dict.fromkeys(chaves, valor_padrao)

# Imprimindo o conteúdo do novo dicionário usando items()
print("Conteúdo do novo dicionário (items):", novo_dicionario.items())

# Imprimindo apenas as chaves do novo dicionário usando keys()
print("Chaves do novo dicionário (keys):", novo_dicionario.keys())

# Imprimindo apenas os valores do novo dicionário usando values()
print("Valores do novo dicionário (values):", novo_dicionario.values())
