import random

# Função para gerar um array de números inteiros aleatórios
def gerar_array_inteiros(tamanho):
    return [random.randint(1, 100) for _ in range(tamanho)]

# Função para gerar um array de strings aleatórias (exemplo: nomes)
def gerar_array_strings(tamanho):
    nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Beatriz', 'Lucas', 'Julia', 'Rafael', 'Amanda', 'Gabriel', 'Fernanda', 'Rodrigo', 'Mariana', 'Felipe']
    return random.sample(nomes, tamanho)

# Array de números inteiros
numeros = gerar_array_inteiros(15)
print("Array original de números:", numeros)

# Ordenação crescente
numeros.sort()
print("Array ordenado de forma crescente:", numeros)

# Ordenação decrescente
numeros.sort(reverse=True)
print("Array ordenado de forma decrescente:", numeros)

# Array de strings (nomes)
nomes = gerar_array_strings(15)
print("\nArray original de nomes:", nomes)

# Ordenação alfabética crescente
nomes.sort()
print("Array ordenado em ordem alfabética crescente:", nomes)

# Ordenação alfabética decrescente
nomes.sort(reverse=True)
print("Array ordenado em ordem alfabética decrescente:", nomes)