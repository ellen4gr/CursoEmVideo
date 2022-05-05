# crie um programa que mostre quanto de dinheiro um pessoa tem e quantos dolares ela pode comprar.
# dollar = US$1,00 = R$3,27
real = float(input('Quantos reais tem na carteira? R$'))
dolar = real/3.27
print('Com {:.2f} reais, você comprará {:.2f} dolars'.format(real, dolar))
