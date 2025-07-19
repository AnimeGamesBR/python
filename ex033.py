n1 = float(input('Digite o 1° número: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))

if n1 > n2 > n3:
    print(f'Maior: {n1}')
    print(f'Menor: {n3}')
elif n3 > n2 > n1:
    print(f'Maior: {n3}')
    print(f'Menor: {n1}')
elif n2 > n1 > n3:
    print(f'Maior: {n2}')
    print(f'Menor: {n3}')
elif n2 > n3 > n1:
    print(f'Maior: {n2}')
    print(f'Menor: {n1}')
elif n1 == n2 > n3:
    print(f'Maiores: {n1} e {n2} são iguais.')
    print(f'Menor: {n3}')
elif n1 == n3 > n2:
    print(f'Maiores: {n1} e {n3} são iguais.')
    print(f'Menor: {n2}')
elif n2 == n3 > n1:
    print(f'Maior: {n2}')
    print(f'Menores: {n1} e {n3} são iguais.')
elif n1 == n2 < n3:
    print(f'Maior: {n3}')
    print(f'Menores: {n1} e {n2} são iguais.')
elif n1 == n3 < n2:
    print(f'Maior: {n2}')
    print(f'Menores: {n1} e {n3} são iguais.')
elif n2 == n3 < n1:
    print(f'Maior: {n1}')
    print(f'Menores: {n2} e {n3} são iguais.')
elif n1 == n2 == n3:
    print('Os três números são iguais.')
