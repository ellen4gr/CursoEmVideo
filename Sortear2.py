import random

a1 = str(input('Nome do 1º alauno: ')),
a2 = str(input('Nome do 2º alauno: ')),
a3 = str(input('Nome do 3º alauno: ')),
a4 = str(input('Nome do 4º alauno: ')),
listaAlunos = [a1, a2, a3, a4]
# suffle embaralha
random.shuffle(listaAlunos)
print('A ordem de apresentação: {}'.format(listaAlunos))
