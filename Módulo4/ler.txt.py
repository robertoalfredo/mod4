# Supondo que o arquivo txt esteja no mesmo diretório e se chame 'meu_arquivo.txt'
# E que ele já tenha sido criado e preenchido com algum conteúdo

# Abrindo o arquivo e armazenando seu conteúdo em uma variável
arquivo = open('meu_arquivo.txt', 'r')
conteudo_completo = arquivo.read()

# Fechando o arquivo (importante para liberar recursos)
arquivo.close()

# Imprimindo o conteúdo completo
print("Conteúdo completo do arquivo:")
print(conteudo_completo)

# Imprimindo a primeira linha
print("\nPrimeira linha do arquivo:")
print(conteudo_completo.splitlines()[0])

# Imprimindo os 3 primeiros caracteres
print("\nOs 3 primeiros caracteres:")
print(conteudo_completo[:3])

# Usando a instrução 'with' para abrir e fechar o arquivo automaticamente
with open('meu_arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print("\nConteúdo do arquivo usando 'with':")
    print(conteudo)