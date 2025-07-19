s = float(input('Digite seu salário: '))

if s <= 1250.00:
    print(f'Seu novo salário é R${s + s * 15/100:.2f}')
else:
    print(f'Seu novo salário é R${s + s * 10/100:.2f}')
