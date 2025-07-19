f = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')

print(f'O inverso de {f} é {f[::-1]}! ')
if f[::-1] == f:
    print('Está frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')
