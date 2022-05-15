''' Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o 
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''
from random import randint
v = 0
while True:
    num1 = int(input('Escolha um numero: '))
    numEscolhido = randint(1, 11)
    soma = num1 + numEscolhido
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Escolha impar ou par [P / I]')).strip().upper()[0]
    print(
        f'O número digitado foi: {num1}, o número do computador foi: {numEscolhido}')
    if escolha == 'P':
        if soma % 2 == 0:
            print('Você GANHOU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif escolha == 'I':
        if soma % 2 == 1:
            print('Você GANHOU')
            v += 1
        else:
            print('Você PERDEU')
            break
print(f'Você venceu {v} vezes ao todo! ')
