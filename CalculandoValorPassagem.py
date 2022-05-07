"""Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem cobrando
R$ 0,50 poe km para viagens de até 200 km e R$ 0,45 para viagens mais longas."""
distancia = float(input("Quantos km de distância? "))
if distancia <= 200:
    valorPassagem = (distancia * 0.50)
    
else:
    valorPassagem = (distancia * 0.45)
print('O valor será R$ {:.2f}'.format(valorPassagem))
