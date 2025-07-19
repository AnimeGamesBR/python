tupla = (int(input('Digite um valor: ')),
         int(input('Digite mais um: ')),
         int(input('Digite mais um: ')),
         int(input('Digite mais um: ')))

print(tupla)

print(f'O número 9 apareceu {tupla.count(9)} vezes!' if tupla.count(9) != 1 else f'O número 9 apareceu {tupla.count(9)} vez!')

if 3 in tupla:
    print(f'O número 3 aparece primeiro na {tupla.index(3) + 1}° posição!')
else:
    print(f'O número 3 não apareceu!')

print('Os números pares foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
