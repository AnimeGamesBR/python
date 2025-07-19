"""from random import randint
from time import sleep
npc = randint(1, 3)
print('-' * 40)
print('JOKENPÔ')
print('-' * 40)
sleep(0.4)
print('O computador está pensando...')
sleep(3)
print('O computador já escolheu o dele, sua vez!')
sleep(0.4)
print('-' * 40)
sleep(0.4)
player = str(input('Escolha pedra, papel ou tesoura: ')).strip().upper()

if player == 'PEDRA':
    player = 1
elif player == 'PAPEL':
    player = 2
elif player == 'TESOURA':
    player = 3
sleep(0.4)
print('Decidindo o vencedor...')
sleep(2)

if npc == 1:
    npc = 'PEDRA'
elif npc == 2:
    npc = 'PAPEL'
elif npc == 3:
    npc = 'TESOURA'

if npc == 'PEDRA' and player == 'TESOURA' or npc == 'PAPEL' and player == 'PEDRA':
    print(f'Você perdeu, o computador escolheu {npc}.')
elif npc == 'PAPEL' and player == 'PEDRA':
    print(f'Você perdeu, o computador escolheu {npc}.')
elif npc == 'TESOURA' and player == 'PAPEL':
    print(f'Você perdeu, o computador escolheu {npc}.')
elif player == 'PEDRA' and npc == 'TESOURA':
    print(f'Parabéns! Você venceu, o computador escolheu {npc}.')
elif player == 'PAPEL' and npc == 'PEDRA':
    print(f'Parabéns! Você venceu, o computador escolheu {npc}.')
elif player == 'TESOURA' and npc == 'PAPEL':
    print(f'Parabéns! Você venceu, o computador escolheu {npc}.')
else:
    print(f'Empate! O computador escolheu {npc}.')
sleep(1)"""

from random import choice
from time import sleep
opcoes = ['pedra', 'papel', 'tesoura']
npc = choice(opcoes)

print('-=' * 20)
print('\033[36mJOKENPÔ\033[m')
print('-=' * 20)
sleep(0.4)

print('\033[33mO computador está pensando', end='')
sleep(0.75)
print('.', end='')
sleep(0.75)
print('.', end='')
sleep(0.75)
print('.')
sleep(0.75)

print('O computador escolheu o dele, sua vez!')
sleep(0.4)
print('\033[m-=' * 20)
sleep(0.4)

player = str(input('\033[33mEscolha pedra, papel ou tesoura: ')).strip().lower()

if player not in opcoes:
    print('Opção inválida. Tente novamente.')
else:
    sleep(0.4)
    print('\033[1;35mJO\033[m', end='')
    sleep(1)
    print('\033[1;31mKEN\033[m', end='')
    sleep(1)
    print('\033[1;34mPÔ!!!\033[m')
    print(f'\033[33mVocê escolheu\033[m \033[1;31m{player}\033[m \033[33me o computador escolheu\033[m \033[1;34m{npc}\033[m\033[33m.\033[m')

    if player == npc:
        print('\033[1;35mEMPATE!')
    elif (player == 'pedra' and npc == 'tesoura') or \
            (player == 'papel' and npc == 'pedra') or \
            (player == 'tesoura' and npc == 'papel'):
        print('\033[1;35mVocê venceu! Parabéns!')
    else:
        print('\033[1;35mVocê perdeu!')
sleep(1)
