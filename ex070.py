nome = maisbarato = continuar = ''
preco = total = mais1000 = maisb = cont = 0

print('[ LOJA DO SERJÃO ]')
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    print('-' * 30)
    total += preco
    cont += 1
    if preco > 1000:
        mais1000 += 1
    if cont == 1:
        maisb = preco
        maisbarato = nome
    else:
        if preco < maisb:
            maisb = preco
            maisbarato = nome

    continuar = str(input('Deseja continuar [S/N]? '))
    while continuar not in 'SsNn':
        print('Seleção incorreta. Por favor selecione uma opção válida.')
        continuar = str(input('Deseja continuar [S/N]? '))
    if continuar in 'Nn':
        break

print('=-=' * 20)
print(f'O total gasto com a compra foi R${total:.2f}!')
print(f'Um total de {mais1000} produtos custam mais de R$1000,00!' if mais1000 != 1 else f'Apenas {mais1000} produto custa mais de R$1000,00!')
print(f'O nome do produto mais barato é "{maisbarato.capitalize()}", custando R${maisb:.2f}!')
