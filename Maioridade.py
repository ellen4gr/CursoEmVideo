"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores."""
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    dataNascimento = int(
        input('Em que ano a {} pessoa nasceu? '.format(pessoa)))
    idade = atual - dataNascimento
    if idade >= 18:
        print('Essa pessoa é maior')
        maior += 1
    else:
        print('Essa pessoa é menor ')
        menor += 1
print("Ao todo tivemos  {} pessoas maiores de idade". format(maior))
print("Ao todo tivemos  {} pessoas menor de idade". format(menor))
