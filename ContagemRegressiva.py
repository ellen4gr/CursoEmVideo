""" Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo
de 10 até 0, com uma pausa de 1 seg entre eles."""
from time import sleep
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('BOOOM')

