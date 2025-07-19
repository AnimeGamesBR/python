s = 0
cont = 0

for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:
        s += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {s}!')
