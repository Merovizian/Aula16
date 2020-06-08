import random
print(f"\033[;1m{'Desafio 074 - Tuplas com numeros aleatórios':*^70}\033[m")

# Cria uma lista para ir colocando os números sem precisar pré fixá-los
lista = ' '
# Pergunta a quantidade maxima de elementos da lista
quantidade = int(input("Informe a quantidade de números: "))
# Pergunta qual o valor maximo de cada elemento randomizado
valor = int(input("Qual o valor máximo dos números gerados: "))

# Esse for cria cada elemento da lista de forma randomica com o limite de elementos imposta pelo Usuario
for c in range (0, quantidade):
    lista = lista.strip()
    # A lista não aceita adicionar inteiro, então colocamos os numeros randomizados como STR
    lista += str(random.randint(0,valor))
    if c < quantidade-1:
        lista += ','

# Aqui separamos em lista os elementos que estão entre virgula para assim criar uma lista de elementos
lista = lista.split(',')
# Transformamos a lista em TUPLA
tupla = tuple(lista)
print(tupla)
print(f"O maior número é o {max(tupla)}")
print(f"O menor número é o {min(tupla)}")