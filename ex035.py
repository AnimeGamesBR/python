n1 = float(input('Digite o comprimento do 1° lado: '))
n2 = float(input('Digite o comprimento do 2° lado: '))
n3 = float(input('Digite o comprimento do 3° lado: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Estes comprimentos podem formar um triângulo.')
else:
    print('Estes comprimentos não podem formar um triângulo.')
