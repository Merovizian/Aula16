#Tuplas é uma lista de elementos de um mesmo tipo, juntos por '()'
lista = ('carne','Arroz','Feijão',"Macarrão")
lista2 = (1,2,6,7,4,5,3,0,9,8,0,2,5)
print(lista)
print()

#Pode ser separado por indices:
print(lista[0])
print(lista[-1])
print(lista[2:0:-1])
print()

# Uma forma de imprimir valores FOR:
for c in lista:
    print(c)
print()

# Uma forma de imprimir valores FOR:
for c in range(0, len(lista)):
    print(lista[c])
print()

# Uma forma de imprimir valores FOR:
for pos, c in enumerate(lista):
    print(f"{c} na posição {pos}")
print()

# Colocar em ordem por 'sorted':
print(sorted(lista))
print(sorted(lista2))
print()

# Manipulando tuplas:
print(lista+lista2)
print()

# Contando a quantidade de um determinado elemento:
print(lista.count('carne'))
print(lista2.count(0))
print()

# indice de determinado elemento:
print(lista2.index(0))
print(lista2.index(0,8))
print()



