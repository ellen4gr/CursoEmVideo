"""Leia um programa que leia a velocidade de um carro. Se ele ultrapassar 80 Km/h nos mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite. """

vel = float(input('\nQual a velocidade do carro? '))
if vel > 80:
    print('\nVocê ultrapassou o limite de velocidade de 80km/h')
    multa = (vel - 80) * 7
    print('\nO valor da multa será R${:.2f}'.format(multa))
else:
    print("\nDentro do limite de velocidade")
