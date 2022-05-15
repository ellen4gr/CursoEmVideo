''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário 
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi 
a soma entre eles. '''
soma = cont = 0
while True:
    num = int(input('Digite um número inteiro [ Digite 999 para sair]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos números: {soma}')
print(f'A quantidade de números digitados: {cont}')
