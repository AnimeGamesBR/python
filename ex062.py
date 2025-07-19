'''print('[ \033[1;4;35mProgressão Aritmética\033[m ]')
pt = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))
c = 10

print('=-=' * 40)
while c != 0:
    print(f'{pt}', end=' → ')
    pt += r
    c -= 1
    if c == 0:
        c = int(input('Você deseja mostrar mais alguns termos? \n[ digite 0 para encerrar ]: '))
        print('=-=' * 40)
print('Programa encerrado.')'''

print('[ \033[1;4;35mProgressão Aritmética\033[m ]')
pt = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))
total = 0
c = 1
mais = 10

print('=-=' * 40)
while mais != 0:
    total += mais
    while c <= total:
        print(f'{pt}', end=' → ')
        pt += r
        c += 1
    print('PAUSA')
    mais = int(input('Digite quantos termos você quer mostrar a mais: '))
print(f'A progressão terminou com um total de {total} termos.')
