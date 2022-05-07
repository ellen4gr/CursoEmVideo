"""Escreva um programa que pergunte o salario de um funcionário e calcule o valor de seu aumento. 
Para salarios supereiore a R$ 1.200,00, calcule um aumento de 10%. Para os inferiores ou iguais o aumento 
é de 15%. """
salario = float(input('Qual seu salário? '))
if salario > 1.200:
    #salario = (salario * 10) / 100
    salarioNovo = salario * 0.10
    salarioNovo = salarioNovo + salario
    print('\n1Seu salário com reajuste R$ {:.4f}'.format(salarioNovo))
else:
    salarioNovo = salario * 0.15
    salarioNovo = salarioNovo + salario
    print('\nSeu salário com reajuste R${:.4f}'.format(salarioNovo))
