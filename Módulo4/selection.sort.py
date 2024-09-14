import random

# Criando um array com 15 números aleatórios
array = [random.randint(1, 100) for _ in range(15)]

# Imprimindo o array original
print("Array original:", array)

# Algoritmo Selection Sort
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    # Trocando os elementos
    array[i], array[min_index] = array[min_index], array[i]

# Imprimindo o array ordenado
print("Array ordenado:", array)