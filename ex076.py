print('{:^46}'.format('[ \033[1;4mMercado do Seu Zé\033[m ]'))
tupla = ('Calça', 40,
         'Cobertor', 30,
         'Camisa', 35,
         'Rosas', 10)

for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end=' ')
    if pos % 2 == 1:
        print(f'R${tupla[pos]:>6.2f}')
