set_inicial = {11, 12, 13, 14}
# Lembrar que o comando set é dado a ordem dos elementos entre chaves {  }
print(set_inicial)
set_inicial.add(15)
print(set_inicial)

set2 = {1, 2, 3, 4, 5}
set_inicial.update(set2)
print(set_inicial)

set_inicial.discard(13)
print(set_inicial)

set3 = {20, 21, 23, 1, 2}
print(set3)

set4 = set_inicial.union(set3)
print(set4)
#Na linha 17 eu criei um novo SET para fazer a união do set inicial e do set3.

set4 = set3.intersection(set_inicial)
print(set4)

set4 = set3.difference(set_inicial)
print(set4)

set4 = set3.symmetric_difference(set_inicial)