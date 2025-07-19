'''p = float(input('Digite o preço normal do produto: '))
print('-' * 50, '\ndinheiro/cheque = 10% de desconto \ncartão = 5% de desconto \n2x no cartão = Preço normal \n3x ou mais no cartão = 20% de juros')
print('-' * 50)
cp = str(input('Digite a condição de pagamento conforme os exemplos acima: ')).strip().lower()

if cp == 'dinheiro' or cp == 'cheque':
    print(f'O valor do produto fica em R${p - p * 10/100:.2f} de acordo com a condição selecionada.')
elif cp == 'cartão' or cp == 'cartao':
    print(f'O valor do produto fica em R${p - p * 5/100:.2f} de acordo com a condição selecionada.')
elif cp == '2x no cartão' or cp == '2x' or cp == '2x no cartao':
    print(f'O valor do produto fica em R${p:.2f} de acordo com a condição selecionada.')
else:
    print(f'O valor do produto fica em R${p + p * 20/100:.2f} de acordo com a condição selecionada.')'''

p = float(input('Digite o preço normal do produto: '))
print('-' * 50)
print('''[ 1 ] Dinheiro/cheque à vista
[ 2 ] Cartão à vista
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
print('-' * 50)
cp = int(input('Digite a condição de pagamento selecionada conforme os exemplos acima: '))
total = p

if cp == 1:
    total = p - (p * 10/100)
    print(f'O valor do produto fica em R${total:.2f} à vista.')
elif cp == 2:
    total = p - (p * 5/100)
    print(f'O valor do produto fica em R${total:.2f} à vista.')
elif cp == 3:
    total = p
    parcelado = p / 2
    print(f'O valor do produto fica parcelado em 2x de R${parcelado:.2f} sem juros no cartão.')
elif cp == 4:
    total = p + (p * 20/100)
    parcela = int(input('Digite em quantas parcelas você deseja comprar o produto: '))
    print(f'O valor do produto fica em {parcela}x de R${total / parcela:.2f} com juros no cartão.')
else:
    print('Opção inválida. Tente novamente.')
print(f'Seu produto de R${p:.2f} vai custar R${total:.2f}!')
