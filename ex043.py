peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
IMC = peso / altura ** 2

print('-'*20)
if IMC < 18.5:
    print('Abaixo do peso.')
elif IMC < 25:
    print('Peso ideal.')
elif IMC < 30:
    print('Sobrepeso.')
elif IMC < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')
print(f'Seu IMC é {IMC:.2f}!')
print('-'* 20, '\nTabela de IMC: \nAbaixo de 18.5 = Abaixo do peso \nEntre 18.5 e 25 = Peso ideal \n25 até 30 = Sobrepeso \n30 até 40 = Obesidade \nAcima de 40 = Obesidade mórbida')
