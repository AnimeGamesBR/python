lista = []

while True:
    a = int(input('Digite um valor: '))
    if a in lista[:]:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(a)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
lista.sort()

print('\n[ \033[1;4;36mResultado da Lista\033[m ]')
print('Lista: ', end='')
for v in lista:
    print(f'{v}', end=' ')
