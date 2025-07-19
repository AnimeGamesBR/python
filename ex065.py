f = ''
s = c = ma = n = 0
me = 999999

while f != 'N':
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c >= 2:
        f = str(input('Deseja continuar? [ S / N ]: ')).upper().strip()
    if ma > n:
        ma = ma
    elif ma < n:
        ma = n
    if me < n:
        me = me
    elif me > n:
        me = n

print(f'Média dos valores: {s / c}')
print(f'Maior valor: {ma} \nMenor valor: {me}')
