# Faça um algoritmo que leia o salário de um funcionário e mostre seu salário com 15% de aumento
salario = float(input('Qual seu atual salário? '))
NovoSalario = salario * 0.15
print('Seu novo salário é {:.2f}'.format(NovoSalario + salario))
