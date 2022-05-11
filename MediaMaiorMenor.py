"""Desenvolva um progrma que leia o nome, idade e sexo de 4 pessoas. No final  do programa, mostre:
A media de idade do grupo. Qual o nome do homem mais velho, quantas mulheres têm menos de 20 anos. """
mediaIdade = 0
somaIdade = 0
for i in range(1 , 3):
    nome = str(input('Qual o nome da {} pessoa? '.format(i)))
    idade= int(input('Qual a idade da {} pessoa? '.format(i)))
    sexo=str(input('Qual o sexo da {} pessoa? '.format(i)))
    somaIdade +=idade
    mediaIdade= somaIdade / len(idade)

print(media) 

#print( nome, idade, sexo )

'''media
maisVelho
menosVinte'''
