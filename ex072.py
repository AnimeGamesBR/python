extenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))

while True:
    if 20 >= n >= 0:
        print(f'O número escolhido, quando escrito por extenso fica \033[1m{extenso[n]}\033[m!')
        continuar = str(input('Deseja continuar [S/N]? ')).strip()
        if continuar in 'Ss':
            n = int(input('Digite um número entre 0 e 20: '))
        if continuar in 'Nn':
            break
    if n > 20 or 0 > n:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print('Programa finalizado.')
