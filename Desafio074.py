import random
print(f"\033[;1m{'Desafio 074 - Tuplas com numeros aleatórios':*^70}\033[m")
lista = ' '
menor = maior = maior_aux = menor_aux = 0
quantidade = int(input("Informe a quantidade de números: "))
valor = int(input("Qual o valor máximo dos números gerados: "))

for c in range (0, quantidade):
    lista = lista.strip()
    lista += str(random.randint(0,valor))
    if c < quantidade-1:
        lista += ','
lista = lista.split(',')
tupla = tuple(lista)
print(tupla)


for c in range (0, quantidade):
    if int(tupla[c]) > maior:
        maior = int(tupla[c])
        maior_aux = c
    if c == 0:
        menor = int(tupla[c])
    if int(tupla[c]) < menor:
        menor = int(tupla[c])
        menor_aux = c
print(f"O maior número é o {maior} na posição {maior_aux}")
print(f"O menor número é o {menor} na posição {menor_aux}")