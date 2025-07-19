'''valor = int(input('Digite um número de 0 a 9999: '))
n = str(valor)

print(f'Unidade: {n[3]} \nDezena: {n[2]} \nCentena: {n[1]} \nMilhar: {n[0]}')'''

valor = int(input('Digite um número de 0 a 9999: '))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
m = valor // 1000 % 10

print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')
