d = int(input('Qual foi a distância da viajem em km? '))

if d <= 200:
    print(f'O preço da viajem foi de R${d * 0.5:.2f}!')
else:
    print(f'O preço da viajem foi de R${d * 0.45:.2f}!')
