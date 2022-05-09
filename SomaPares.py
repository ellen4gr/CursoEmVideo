""" Crie um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado pro ímpar desconsiderar.  """
SomaPar = 0
cont = 0
for i in range(1, 7): # 
    num = int(input('Digite o {} número: '.format(i)))
    if num % 2 == 0:
        SomaPar += num
        cont += 1
print('\nVocê digitou {} pares e a soma dos pares {}'.format(cont, SomaPar))
