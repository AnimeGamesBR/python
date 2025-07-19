n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O primeiro valor é maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('O segundo valor é maior.')
