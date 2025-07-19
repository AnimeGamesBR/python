from random import randint
print('{:=^102}'.format(' \033[1;4;36mPAR OU ÍMPAR\033[m '))
v = player = g = 0

while True:
    cpu = randint(0, 9)

    pi = str(input('Par ou impar? '))
    while pi.strip().upper() != 'PAR' and pi.strip().upper() != 'IMPAR':
        print('Seleção incorreta, por favor selecione par ou impar.')
        pi = str(input('Par ou impar? '))
    player = int(input('O computador pensou em um número de 0 a 9, escolha o seu número e boa sorte: '))
    print('=-=' * 30)
    g = cpu + player
    if g % 2 == 0 and pi.strip().upper() == 'PAR':
        v += 1
        print('Você ganhou!')
    elif g % 2 == 1 and pi.strip().upper() == 'IMPAR':
        v += 1
        print('Você ganhou!')
    else:
        break
    print(f'A soma de {cpu} e {player} dá {g}, que é par.' if g % 2 == 0 else f'A soma de {cpu} e {player} dá {g}, que é ímpar.')
    print('=-=' * 30)
print(f'A soma de {cpu} e {player} dá {g}, que é par.' if g % 2 == 0 else f'A soma de {cpu} e {player} dá {g}, que é ímpar.')
print(f'Você ganhou {v} vezes consecutivas.' if v != 1 else f'Você ganhou apenas {v} vez. Mais sorte da próxima vez...')
