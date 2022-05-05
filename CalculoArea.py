# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))

area = largura * altura
qtdeTinta = area/2

print('Area {:.2f} m² e a quantidade de litros de tinta necessária {:.1f} '.format(
    area, qtdeTinta))
