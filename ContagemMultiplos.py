"""Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se 
encontram no intervalo até 500"""
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma = soma + i
        cont += 1
        # print(i)
print('Soma dos ímpares: {} e a soma de TODOS os valores solicitados é  {}'. format(soma, cont))
