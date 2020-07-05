#Desafio11 - Gerador de senhas

import random
from time import sleep

password = ''.join(random.choice('0123456789ABCDEF') for i in range(16))

print('PROCESSANDO...')
sleep(2)

print(password)


