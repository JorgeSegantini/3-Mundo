#Jokenpo
from random import randint
from time import sleep
print(f'{" Jokenpô ":=^40}')
itens = ('Pedra', 'Papel', 'Tesoura')
print('''
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jog = int(input('Qual é sua jogada? '))
com = randint (0,2)
sleep(1)
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('po!!')
sleep(1)
print('-=' * 18)
print(f'O computador escolheu {itens[com]}')
print(f'O jogador escolheu {itens[jog]}')
print('-=' * 18)
if com == 0:       #Comp jogou pedra 
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('Jogador vence')
    elif jog == 2:
        print('Computador vence')
    else:
        print('Jogada inválida')
elif com == 1: #Comp jogou papel
    if jog == 0:
        print('Computador vence')
    elif jog == 1:
        print('Empate')
    elif jog == 2:
        print('Jogador vence')
    else:
        print('Jogada invalida')
elif com == 2: #Comp jogou teso
    if jog == 0:
        print('Jogador vence')
    elif jog == 1:
        print('Computador vence')
    elif jog == 2:
        print('Empate')
    else:
        print('Jogada invalida')





