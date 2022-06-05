'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
No final moste: 1 - qual o total gasto na compra 2 - quantos produtos custas mais de 1.000 - 3 - qual é o nome do produto
mais barato.'''

prodMaisMil = total = preco = cont = menor = 0
prodMaisBarato = ''
while True:
    produto = str(input('Qual o produto? '))
    preco = float(input('Qual o preço do produto? '))
    cont+=1
    total += preco
    if preco > 1000:
        prodMaisMil+=1
    if cont == 1:
        menor = preco
        prodMaisBarato = produto
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'NS':
        resp = str(
            input('Deseja adicionar mais produtos? [S / N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'\nTotal da compra R$: {total:.2f}')
print(f'\nQuantidade de produtos com valor maior que R$ 1.000: {prodMaisMil}')
print(f'\nO produto mais barato da compra é: {prodMaisBarato}\n')