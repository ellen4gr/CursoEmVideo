"""Desenvolva um progrma que leia o nome, idade e sexo de 4 pessoas. No final  do programa, mostre:
A media de idade do grupo. Qual o nome do homem mais velho, quantas mulheres têm menos de 20 anos. """
mediaIdade = 0
somaIdade = 0
maiorIdade = 0
maisVelhoMasc = 0
nomeMaisVelho = 0
totalFem = 0
for i in range(1, 5):
    nome = str(input('\nQual o nome da {} pessoa? '.format(i)))
    idade = int(input('Qual a idade da {} pessoa? '.format(i)))
    sexo = str(input('Qual o sexo da {} pessoa? [M/F] '.format(i))).upper()
    somaIdade += idade

    if i == 1 and sexo in "Mm":
        maisVelhoMasc = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maisVelhoMasc:
        maisVelhoMasc = idade
        nomeMaisVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalFem += 1

mediaIdade = somaIdade / i
print('\nA media de idade é: {}'.format(mediaIdade))
print('O homem mais velho tem: {} anos e se chama {}'.format(
    maisVelhoMasc, nomeMaisVelho))
print('Ao todo são {} mulheres menores de 20 anos'.format(totalFem))
