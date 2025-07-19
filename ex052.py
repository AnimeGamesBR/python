'''
n = int(input('Digite um número: '))

for c in range(1, n):
    if n % c != 0 and n != 1:
        print('Este número é primo.')
    else:
        print('Este número não é primo.')
'''

n = int(input('Digite um número: '))
cont = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')

print(f'\n\033[mO número {n} foi divisivel {cont} vezes.')
if cont == 2:
    print('O número não é primo.')
else:
    print('O número é primo.')
