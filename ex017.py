'''from math import sqrt

ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
h = sqrt(pow(ca, 2) + pow(co, 2))

print(f'A hipotenusa é equivalente a {h:.2f}, levando em conta os catetos {co:.2f} e {ca:.2f}.')'''


'''ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
h = (ca ** 2 + co ** 2) ** (1/2)

print(f'A hipotenusa é equivalente a {h:.2f}, levando em conta os catetos {co:.2f} e {ca:.2f}.')'''


from math import hypot

ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))
h = hypot(co, ca)

print(f'A hipotenusa é equivalente a {h:.2f}, levando em conta os catetos {co:.2f} e {ca:.2f}.')
