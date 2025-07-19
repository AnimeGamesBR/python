'''sexo = str('')

while sexo not in 'MF':
    sexo = str(input('Digite seu sexo [ M ] / [ F ]: ')).strip().upper()[0]
    if sexo not in 'MF':
        print('Opção inválida. Tente novamente digitando a opção correta!')
    else:
        print('Sexo registrado como masculino com sucesso!' if sexo == 'M' else 'Sexo registrado como feminino com sucesso!')'''

sexo = str(input('Digite seu sexo [ M ] / [ F ]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo registrado como masculino com sucesso!' if sexo == 'M' else 'Sexo registrado como feminino com sucesso!')
