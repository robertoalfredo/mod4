def bubble_sort(array):
  """Implementa o algoritmo de ordenação Bubble Sort.

  Args:
    array: O array a ser ordenado.
  """

  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j + 1]
        array[j + 1] = temp 


# Criando um array de números aleatórios
import random
array = [random.randint(1, 100) for _ in range(15)]

# Aplicando o Bubble Sort
bubble_sort(array)

# Imprimindo o array ordenado
print("Array ordenado:", array)