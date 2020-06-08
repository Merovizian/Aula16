import tupla
print(f"\033[;1m{'Desafio 075 - Valores de uma tupla':*^70}\033[m")

# Utilizo o modulo que criei que serve para criar uma tupla com inumeros elementos
lista = tupla.tuplaint(int(input("Informe a quantidade de números: ")))

# While que cria o menu
while True:
    print('-='*20)
    print(f"Tupla digitada: {lista}")
    print('''    1 - Quantas vezes aparece o valor digitado. 
    2 - Em que posição aparece o valor digitado.
    3 - Quais foram os números pares.''')
    print('-='*20)

    escolha = int(input("Digite uma opção: "))
    if escolha == 1:
        valor = int(input("Informe o Valor: "))
        print(f"O valor {valor} apareceu {lista.count(valor)} vezes.")
        input("Digite enter para continuar...")
    if escolha == 2:
        valor = int(input("Informe o Valor: "))
        if valor in lista:
            print(f"O valor {valor} está primeiramente na posição {lista.index(valor)}")
        else:
            print(f"O valor {valor} não está em {lista}.")
        input("Digite enter para continuar...")
    if escolha == 3:
        print(f"Os PARES da tupla {lista} São: ",end='')
        for c in lista:
            if c % 2 == 0:
                print(c,end=' ')
        print()
        input("Digite enter para continuar...")
