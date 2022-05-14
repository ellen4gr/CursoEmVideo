"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer
ou não continuar a digitar valores. 
 """
qtde = 0
media = 0
menorValor = 0
maiorValor = 0
resposta = ""
soma = 0

while resposta in 'Ss':
    num = int(input('Digite um número inteiro: '))
    soma += num
    qtde += 1
    if qtde == 1:
        maiorValor = menorValor = num
    else:
        if num > maiorValor:
            maiorValor = num
        if num < menorValor:
            menorValor = num
    resposta = str(
        input("Deseja digitar mais valores? [S / N]")).upper().strip()[0]
media = soma / qtde
print('A média dos valores digitados foi: {}'.format(media))
print('O maior valor foi {} e o menor valor foi  {}'.format(maiorValor, menorValor))
