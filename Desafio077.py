print(f"\033[;1m{'Desafio 077 - Vogais nas palavras':*^70}\033[m")
lista = ''
cont = 0
# Cria a lista com os nome inseridos pelo usuário
while True:
    palavra = input("Informe uma palavra: "if cont==0 else "Informe uma palavra ou [Não] para sair: ")
    if palavra.lower() == 'nao':
        break
    lista += palavra + ','
    cont += 1
# Transforma a lista em uma tupla
lista = tuple(lista.split(','))
lista = lista[:len(lista)-1]

print(lista,type(lista))

# O primeiro for serve para abstrair uma palavra
for a in range(0, cont):
    print(f"A Palavra '{str(lista[a]).upper():^20}' tem as vogais:", end=' ')

    # O segundo for é para caçar na palavra abstraída as vogais.
    for b in range(0, len(lista[a])):
        if str(lista[a][b]).lower() in 'aeiouéáàèíìãẽĩõ':
            print(lista[a][b],end=' ')
    print()
