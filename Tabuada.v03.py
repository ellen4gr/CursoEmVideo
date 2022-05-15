'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
O programa será interrompido quando o número solicitado for negativo. '''
while True:
    num = int(
        input('\nDigite o número da tabuada/ [Para sair digite número negativo]: '))
    if num < 0:
        break
    for i in range(0, 11):
        print(f'{num} X {i} = {i*num}')
