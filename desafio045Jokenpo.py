print('***** DESAFIO 044 *****')
print('=' * 30)

from random import randint
from time import sleep

print('Vamos Jogar Jokepo?')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

nome_usuario = str(input('Digite seu nome: '))
print(' - ESCOLHA UM NÚMERO -')

print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')

jogadaUsuario = int(input('Qual a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=-' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('{} jogou {}'.format(nome_usuario, itens[jogadaUsuario]))
print('-=-' * 10)
if computador == 0: # computador jogou PEDRA
    if jogadaUsuario == 0:
        print('ROLOU EMPATE!')
    elif jogadaUsuario == 1:
        print('PARABÉNS! {}, VOCÊ VENCEU!'.format(nome_usuario))
    elif jogadaUsuario == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogadaUsuario == 0:
        print('COMPUTADOR VENCEU!')
    elif jogadaUsuario == 1:
        print('ROLOU EMPATE!')
    elif jogadaUsuario == 2:
        print('PARABÉNS! {}, VOCÊ VENCEU!'.format(nome_usuario))
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #  computador jogou TESOURA
    if jogadaUsuario == 0:
        print('PARABÉNS! {}, VOCÊ VENCEU!'.format(nome_usuario))
    elif jogadaUsuario == 1:
        print('COMPUTADOR VENCEU!')
    elif jogadaUsuario == 2:
        print('ROLOU EMPATE')
    else:
        print('JOGADA INVÁLIDA')
print('-=-' * 10)

