print('[ \033[1;4;35mProgressão Aritmética\033[m ]')
pt = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))
c = 0

print('-=' * 55)
while c <= 10:
    print(pt, end= ' → ')
    pt += r
    c += 1
print('FIM')
