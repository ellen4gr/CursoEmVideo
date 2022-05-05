# Faça um programa que leia um numero int e faça sua tabuada
import math

num = int(input('Digite um numero inteiro: '))
for cont in range(0, 11):
    print(' {} x {} = {}'.format(num, cont, num*cont))
