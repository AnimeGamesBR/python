v = int(input('Digite um número inteiro: '))
print('[ 1 ] para binário. \n[ 2 ] para octal. \n[ 3 ] para hexadecimal.')
bc = int(input('Escolha uma das opções acima: '))

if bc == 1:
    print(f'{v} convertido para binário é igual a {v:b}')
elif bc == 2:
    print(f'{v} convertido para octal é igual a {v:o}')
elif bc == 3:
    print(f'{v} convertido para hexadecimal é igual a {v:x}')
else:
    print('Você não selecionou nenhuma das opções.')
