from time import sleep
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
e = 0

while e != 5:
    print('\033[1m=-=\033[m' * 13)
    e = int(input('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa \nSelecione uma das opções acima: '))
    if e == 1:
        print(f'A soma de {n1} e {n2} é {n1+n2}!')
    elif e == 2:
        print(f'A multiplicação de {n1} e {n2} é {n1*n2}!')
    elif e == 3 and n1 > n2:
        print(f'O maior entre {n1} e {n2} é {n1}!')
    elif e == 3 and n2 > n1:
        print(f'O maior entre {n1} e {n2} é {n2}!')
    elif e == 4:
        n1 = int(input('Digite o novo 1° valor: '))
        n2 = int(input('Digite o novo 2° valor: '))
    elif e == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente selecionando uma das opções abaixo.')
    sleep(2)
print('\033[1m=-=\033[m' * 13)
print('Programa encerrado.')
