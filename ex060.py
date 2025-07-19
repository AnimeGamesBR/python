'''n = int(input('Digite um valor: '))
c = n
f = 1

print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)'''

n = int(input('Digite um valor: '))
c = n
f = 1
print(f'{n}!', end=' = ')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

'''from math import factorial
n = int(input('Digite um número: '))
print(factorial(n))'''