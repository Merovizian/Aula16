print(f"\033[;1m{'Desafio 075 - Produtos e Valores':*^70}\033[m")
lista = ''
c = 0
# Cria uma lista com os dados que serão informados
while True:
    produto = input("Informe o produto: " if c == 0 else "Informe o produto ou [Nao] para Sair: ")
    if (produto.lower()) == 'nao':
        break
    valor = input("Informe o valor do produto: ")
    lista += produto + ',' + valor + ','
    c += 1
# Transforma a lista em uma lista de verdade
lista = lista[:len(lista)-1].split(',')

# Transforma os str de inteiro em inteiro de verdade
for a in range (1, c*2 ,2):
    lista[a] = float(lista[a])

# Transforma a lista em uma TUPLA
lista = (tuple(lista))

# Printa a tabela com os dados e preços na tela.
print('-'*50)
print(f"{'Listagem de Preços':^50}")
print('-'*50)

for a in range (0,c*2,2):
    print(f"{lista[a]:.<38}R${lista[a+1]:>10.2f}")

print('-'*50)
