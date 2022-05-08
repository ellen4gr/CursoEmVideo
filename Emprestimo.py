""" Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30%
do salário ou então o empréstimo será negado.
"""
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
anosPagamento = int(input('Quantos anos irá pagar? '))

# converte anos para meses
anosPagamento = (anosPagamento * 12)
prestacao = (casa / anosPagamento)
# verifica se excede 30% do salário
salarioExecedente = (salario * 30) / 100

if prestacao > salarioExecedente:
    print('Emprestimo Negado, excedeu o limite de 30%' 'do seu salário')
else:
    print('Quantidade de prestações: {} e o valor será R$ {:.2f}'.format(
        anosPagamento, prestacao))
