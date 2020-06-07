import tupla
print(f"\033[;1m{'Desafio 075 - Valores de uma tupla':*^70}\033[m")
cont1 = 0

lista = tupla.tuplaint(int(input("Informe a quantidade de números: ")))
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
        for c in lista:
            if c == valor:
                cont1 += 1
        print(f"O valor {valor} apareceu {cont1} vezes.")
        cont1 = 0
        input("Digite enter para continuar...")
    if escolha == 2:
        valor = int(input("Informe o Valor: "))
        print(f"O valor {valor} está primeiramente na posição {lista.index(valor)}")
        input("Digite enter para continuar...")
    if escolha == 3:
        print("Os seguintes valores são PAR: ")
        for c in lista:
            if c % 2 == 0:
                print(c,end=' ')
        print()
        input("Digite enter para continuar...")
