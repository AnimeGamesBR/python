from math import floor, ceil

w = float(input('Digite a largura: '))
h = float(input('Digite a altura: '))
a = h * w
l = a / 2

print(f'A quantidade necessária de tinta para pintar um muro de {a}m² é aproximadamente {ceil(l)}l!')
