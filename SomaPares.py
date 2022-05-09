""" Crie um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado pro ímpar desconsiderar.  """
SomaPar = 0
for i in range(3):
    num = int(input('Digite o número: '))
    if num % 2 == 0:
        SomaPar = SomaPar + num
print('\nA soma dos pares {}'.format(SomaPar))
