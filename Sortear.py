# Programa que sorteia 1 entre 4 alunos, e que leia seus nomes
import random

a1 = str(input('Nome do 1º alauno: ')),
a2 = str(input('Nome do 2º alauno: ')),
a3 = str(input('Nome do 3º alauno: ')),
a4 = str(input('Nome do 4º alauno: ')),
listaAlunos = [a1, a2, a3, a4]
alunoEscolhido = random.choice(listaAlunos)
print('O aluno sorteado é: {}'.format(alunoEscolhido))
