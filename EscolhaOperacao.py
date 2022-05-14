""" Crie um programa que leia dois valores e mostre um menu na tela
[1] - Soma
[2] - Multiplicação
[3] - Maior
[4] - Novos números
[5] - Sair do programa
O programa deverá realizara operação solicitada em cada caso. 
"""

num1 = int(input('Escolha um número: '))
num2 = int(input('Escolha outro  número: '))

soma = 0
mult = 0
maior = 0
novosNum = 0
escolha = 0

while escolha != 5:
    print('''    [1] - Soma
    [2] - Multiplicação
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa\n''')
    escolha = int(input('Qual a opção escolhida? '))
    if escolha == 1:
        soma = num1 + num2
        print("\nA soma dos número é {}\n".format(soma))
    elif escolha == 2:
        mult = num1 * num2
        print("\nA multiplicação é {}\n".format(mult))
    elif escolha == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print("\nO maior número é {}\n".format(maior))
    elif escolha == 4:
        num1 = int(input('Escolha um número: '))
        num2 = int(input('Escolha outro  número: '))
    else:
        print('Opção inválida. Tente novamente')
