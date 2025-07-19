print('-' * 26)
print('[ \033[1;36mSEQUÊNCIA DE FIBONACCI\033[m ]')
print('-' * 26)
n = int(input('Digite um número inteiro: '))
p = 0
a = 0

print('~' * 26)
while n != 0:
    print(f'{p}', end=' → ')
    p += a
    a = p - a
    n -= 1
    if p == 0:
        p += 1
print('FIM')
