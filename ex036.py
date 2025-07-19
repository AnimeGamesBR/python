vc = float(input('Digite o valor da casa: R$'))
sc = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite em quantos anos ele vai pagar: '))
pm = vc / anos / 12

if pm > sc * 30/100:
    print(f'Seu empréstimo foi negado. Seu salário de R${sc:.2f} está abaixo do requisitado para o empréstimo.')
else:
    print(f'Seu empréstimo foi aceito. O valor a ser pago mensalmente será R${pm:.2f}!')
