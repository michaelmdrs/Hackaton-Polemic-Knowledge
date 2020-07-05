#Desafio1 - Conversor de Graus Celsius para Farenheint e Vice-versa

desafio = 'Conversor de Graus Celsius para Farenheint e Vice-versa'

print('{:=^20}\n'.format(desafio))

grausCelsius = float(input('Informe a temperatura em °C: '))

farenheit = (grausCelsius * 1.8000) + 32 #Outra formula e ((9 * grausCelsius) / 5) + 32

print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(grausCelsius, farenheit))

print('-' * 30)

grausFahrenheit = float(input('Informe a temperatura em °F: '))

celsius = (grausFahrenheit - 32) / 1.8000

print('A temperatura de {:.1f} corresponde a {:.1f} °C'.format(grausFahrenheit, celsius))
