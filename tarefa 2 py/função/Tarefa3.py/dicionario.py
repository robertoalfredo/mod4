dicio = {
  1: 'python',
  2: 'java',
  3: 'php'
}
#Declara o Dicionário e coloca entre "Chaves {}"
# Lembrar que deve declarar os elementos utilizando os : " " e a vírgula no final dos elementos.
print('Conteúdo do meu dicionário é: ', dicio) 
print('O tipo de dados do dicionário é: ', type(dicio))

valor = dicio.get(1)
print('valor da chave 1 é: ', valor)
#Declaro uma variável para chamar o valor da chave.

dicionario_frutas = dict ({
    #Utiliza-se o ({}) no Dict quando for abrir um dicionário, sendo o parênteses que corresponde ao comando dict, e as chaves que corresponde ao comando do dicionário.
    1: {"nome": "Limão", "tipo": "Ácida"},
    2: {"nome": "Laranja", "tipo": "Ácida"},
    3: {"nome": "Manga", "tipo": "Semiácida"},
    4: {"nome": "Maçã", "tipo": "SemiAcida"},
    5: {"nome": "Banana", "tipo": "Doce"},
    6: {"nome": "Mamão", "tipo": "Doce"}
})
#As chaves são chamadas por números, abre as { } que corresponde ao dicionário, e vai lançando chave por chave,
# Ex -> chave "nome e tipo"
# Lembrar também que para declarar o elemento, colocar os dois pontos : 
# Lembrar também de separar as chaves pela ","
for chave, valor in dicionario_frutas.items():
    print ('Chave 1 - Nome: ', dicionario_frutas[1]["nome"], ", Tipo: ", dicionario_frutas[1]["tipo"])
    print ('Chave 2 - Nome: ', dicionario_frutas[2]["nome"], ", Tipo: ", dicionario_frutas[2]["tipo"])
    print ('Chave 3 - Nome: ', dicionario_frutas[3]["nome"], ", Tipo: ", dicionario_frutas[3]["tipo"])
    print ('Chave 4 - Nome: ', dicionario_frutas[4]["nome"], ", Tipo: ", dicionario_frutas[4]["tipo"])
    print ('Chave 5 - Nome: ', dicionario_frutas[5]["nome"], ", Tipo: ", dicionario_frutas[5]["tipo"])
else: print("ACABOU")

# for chave, valor in: Esta é a parte do laço for que define duas variáveis, chave e valor.
# Como explicado, .items() retorna uma coleção de tuplas onde cada tupla é um par (chave, valor) do dicionário.
