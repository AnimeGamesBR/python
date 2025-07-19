lista = []
listaP = []
listaI = []

while True:
    num = int(input(f'Digite o {len(lista) + 1}° valor: '))
    lista.append(num)
    if num % 2 == 0:
        listaP.append(num)
    else:
        listaI.append(num)
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'A lista original é: {lista}')
print(f'A lista com apenas os números pares é: {listaP}' if len(listaP) != 0 else 'Não existem números pares na lista.')
print(f'A lista com apenas os números ímpares é: {listaI}' if len(listaI) != 0 else 'Não existem números ímpares na lista.')
