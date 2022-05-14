''' Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex 5x4x3x2x1x3x2x1'''
i = 0
fatorial = 1
num = int(input('Digite um número: '))
cont = num
while cont > 0:
    print('{}'.format(cont), end='')
    print(' X ' if cont > 1 else' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))
