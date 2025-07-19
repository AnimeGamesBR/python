s = 0
cont = 0

for c in range(0, 6):
    cont += 1
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(f'Desconsiderando os números ímpares que você digitou, a soma dos {cont} números digitados é {s}!')
