"""Faça um programa que leia o sexo de uma pessoa, mas só aceite valores M ou F. Caso esteja errado peça
a digitação novamente até ter um valor correto. """

resposta = ''
sexo = str(input('Qual seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado errado! Digite o valor correto: '))
print('\nO sexo digitado foi {}'.format(sexo))
