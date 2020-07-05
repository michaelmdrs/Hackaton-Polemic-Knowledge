#Desafio10 - Programa que calcula a fórmula de bhaskara

import math

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

delta = b ** 2 - 4 * a * c

raiz_quadrada1 = (-b + math.sqrt(delta)) / (2 * a)
raiz_quadrada2 = (-b - math.sqrt(delta)) / (2 * a)

print('Valor da Raiz 1 é: ', raiz_quadrada1)
print('Valor da Raiz 2 é: ', raiz_quadrada2)
