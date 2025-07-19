i = 0
s = 0
c = -1
p = '0'

print('Digite [ fim ] para encerrar a sequência.')
while p != 'FIM':
    i = int(p)
    s += i
    c += 1
    p = str(input('Digite um número: ')).upper()
print(f'A quantidade de números digitados foi {c} e a soma entre eles é {s}!')
