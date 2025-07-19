n1 = float(input('Digite o comprimento do primeiro seguimento: '))
n2 = float(input('Digite o comprimento do segundo seguimento: '))
n3 = float(input('Digite o comprimento do terceiro seguimento: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1 == n2 == n3:
    print('Estes comprimentos formam um triângulo Equilátero.')
elif n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1 == n2 or n2 == n3 or n3 == n1:
    print('Estes comprimentos formam um triângulo Isósceles.')
else:
    print('Estes comprimentos formam um triângulo Escaleno.')
