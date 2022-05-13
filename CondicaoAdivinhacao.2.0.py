"""Escreva um programa que faça o computador "pensar" em número inteiro antes de 0 5 e peça para o usuário 
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário 
venceu ou perdeu."""

# VERSÃO 2 - Utilizando While

"""Escreva um programa que faça o computador "pensar" em número inteiro entre  0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

import random
i = 0
num1 = int(input("\nDigite um numero de 0 a 10: "))
num2 = (random.randint(0, 2))

while num1 != num2:
    num1 = int(input("\nVocê Perdeu! Digite novamente: "))
    i = i+1
if num1 == num2:
    print("\nVocê Venceu! Seu palpite foi: {}, mesmo número escolhido pelo computador.".format(num2))
print('\nForam necessário {} palpites para você vencer! \n'.format(i+1))
