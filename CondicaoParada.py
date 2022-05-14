'''Crie um programa que leia vários números  interiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final mostre quantos número foram digitados e qual foi a 
soma entre eles. menos o 999 '''
cont = 0
num = 0
soma = 0
num = int(input('Digite um número inteiro [Para parar 999]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número inteiro [Para parar 999]: '))
print('Você digitou {} números'.format(cont))
print(' A soma dos números é {}'.format(soma))
