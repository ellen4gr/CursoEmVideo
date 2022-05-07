"""Escreva um programa que faça o computador "pensar" em número inteiro antes de 0 5 e feça para o usuário 
tentardescobri qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário 
venceu ou perdeu."""

import random

num1 = int(input("\nDigite um numero: "))
# random de numero inteiro
num2 = (random.randint(0, 5))
if num1 == num2:
    print(num2)
    print("\nVocê Venceu!")
else:
    print("\nVocê Perdeu!")

print('\nNúmero pensado pelo computador: {}'.format(num2))
print('\nNúmero escolhido por você: {}'.format(num1))