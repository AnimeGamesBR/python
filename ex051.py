print('[ \033[1;4;35mProgressão Aritmética\033[m ]')
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

print('-=' * 55)
for c in range(pt, pt + r * 10, r):
    print(c, end= ' → ')
print('FIM')

