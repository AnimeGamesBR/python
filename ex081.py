lista = []

while True:
    num = int(input(f'Digite o {len(lista) + 1}° valor: '))
    lista.append(num)
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'{len(lista)} números foram digitados!' if len(lista) != 1 else f'{lista} número foi digitado!')
print(f'A lista, em ordem decrescente fica: {sorted(lista, reverse=True)}!')
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)}!')
else:
    print('O valor 5 não foi digitado.')
