print(f"\033[;1m{'Desafio 072 - Numeros por extenso':*^70}\033[m")
numeros = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze')

while True:
    valor = int(input("Digite um valor  de 0 a 15: "))
    if valor in range (0,16):
        print(f"\033[1;33mVocê digitou o número {numeros[valor]}\033[m")
    else:
        print("\033[1;31mValor Errado!\033[m")
    if (input("Deseja continuar? [N/S]: ").lower()[0]) == 'n':
        break


