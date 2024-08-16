primeira_tupla = (1, 2, 3, "Olá tupla")
print(primeira_tupla)
indice = primeira_tupla.index(3)
print("O indice número 4 da tupla é: ", indice)
# Declara uma variável chamado: Indice.
#Juntamente com o comando "Index", com o objetivo de verificar o elemento da tupla

if 3 in primeira_tupla:
    print("A tupla contém o elemento 3")
else:
    print('A tupla não contém o elemento 3')
# Utiliza o comando If in, para saber se possui o elemento 3 da tupla, utilizando uma condição, se sim e se não.

if 33 in primeira_tupla:
    print('A tupla contém o elemento 33.')
else:
    print("A tupla não contém o elemento 33.")