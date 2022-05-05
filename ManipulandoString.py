# crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras mauiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Qual seu nome completo? ')).strip()
print('Nome com letras maiúsculas: {}'.format(nome.upper()))
print('Nome com letras minúsculas: {}'.format(nome.lower()))
print('Total de letras (sem considerar espaços): {}'.format(
    len(nome)-nome.count(' ')))  # strip tira os espaços
print('Quantas letras tem o primeiro nome: {}'.format(nome.find(' ')))
