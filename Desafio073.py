print(f"\033[;1m{'Desafio 073 - Tabela Brasileirão':*^70}\033[m")
lista = ('Bahia', 'Ceara', 'Fortaleza', 'Atletico Goianiense', 'Goias', 'Atletico Mineiro', 'Athletico Paranaense', 'Coritiba', 'Sport', 'Botafogo', 'Flamengo', 'Fluminense', 'Vasco', 'Gremio', 'Internacional', 'Corinthians', 'Palmeiras', 'Red Bull Bragantino', 'Santos', 'Sao Paulo')
while True:
    print ('-='*20)
    print(f"{'MENU BRASILEIRÃO':^40}")
    print('''    1 - Os 5 primeiros colocados.
    2 - Os ultimos 4 colocados.
    3 - Ordem alfabetica.
    4 - Retorna a posição do time.''')
    print ('-='*20)
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        print('\n'*100)
        print(f"Os 5 primeiros colocados: {lista[:5]}")
        input("Pressione 'Enter' para continuar...")
        print('\n'*100)
    if escolha == 2:
        print('\n' * 100)
        print(f"Os últimos 4 colocados da tabela são: {lista[len(lista)-4:]}")
        input("Pressione 'Enter' para continuar...")
        print('\n' * 100)
    if escolha == 3:
        list2 = (sorted(lista))
        print('\n' * 100)
        print(f"{'Times por ordem alfabética':*^40}")
        for c in list2:
            print(c)
        input("Pressione 'Enter' para continuar...")
        print('\n' * 100)
    if escolha == 4:
        print('\n' * 100)
        lista3 = list(lista)
        for c in range (0, len(lista3)):
            lista3[c] = str(lista3[c]).lower()
            if lista3[c].find(' ') != -1:
                lista3[c] = str(lista3[c][:lista3[c].find(' ')] + lista3[c][lista3[c].find(' ')+1:])
            lista3[c] = lista3[c][:7]
        time = input("Escolha o time para retornar a posição: ")
        time2 = time.lower()
        if time2.find(' ') != -1:
            time2 = time2[:time2.find(' ')] + time2[time2.find(' ')+1:]
        time2 = time2[:7]

        print(f"O time {time} está na {lista3.index(time2)+1} posição!")
        input("Pressione 'Enter' para continuar...")
        print('\n' * 100)
    if escolha not in range(0,4):
        print("\033[1;31mOpção Invalida!\033[m")
        input("Pressione 'Enter' para continuar...")
