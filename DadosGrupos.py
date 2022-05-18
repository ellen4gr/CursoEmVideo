''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:
a- quantas pessoas tem mais de 18 anos
b- quantos homens foram cadastrados
c-quantas mulheres tem menos de 20 anos'''
masculino = feminino = maior18 = 0

while True:
    idade = int(input('Quantos anos você tem? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F]')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        masculino += 1
    if sexo == 'F' and idade < 20:
        feminino += 1
    resposta = ' '
    while resposta not in 'SsNn':
        resposta = str(input('Deseja continuar? [S / N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'\nTotal de pessoas com mais de 18 anos: {maior18}')
print(f'Total de pessoas de sexo masculino: {masculino}')
print(f'Total de pessoas mulheres com menos de 20 anos: {feminino}')
