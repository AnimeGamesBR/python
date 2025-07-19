print('=' * 30)
print('{:^30}'.format('BANCO SLA'))
print('=' * 30)
v = int(input('Qual valor você quer sacar? R$'))
c = 100
tc = 0

while True:
    if v >= c:
        v -= c
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc} cédulas de R${c:.2f}!' if tc != 1 else f'Total de {tc} cédula de R${c:.2f}!')
        if c == 100:
            c = 50
        elif c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if v == 0:
            break
