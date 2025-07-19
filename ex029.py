v = int(input('Digite a velocidade em km/h de um carro: '))

if v > 80:
    print(f'Você foi multado! O valor a ser pago é R${7 * (v - 80):.2f}')
print('Tenha um bom dia! Dirija com segurança!')
